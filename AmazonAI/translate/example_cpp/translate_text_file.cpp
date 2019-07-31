#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/translate/TranslateClient.h>
#include <aws/translate/model/TranslateTextRequest.h>
#include <aws/translate/model/TranslateTextResult.h>

#include <fstream>
#include <iostream>
#include <string>

# define MAX_LINE_LENGTH 5000

int main(int argc, char **argv) {
  if (argc != 4) {
    std::cout << "Usage: translate_text_file 'target language code' 'input file'"
            "'output file'"
         << std::endl;
    return -1;
  }

  const Aws::String target_language = argv[1];
  const std::string input_file = argv[2];
  const std::string output_file = argv[3];

  std::ifstream fin(input_file.c_str(), std::ios::in);
  if (!fin.good()) {
    std::cerr << "Input file is invalid." << std::endl;
    return -1;
  }

  std::ofstream fout(output_file.c_str(), std::ios::out);
  if (!fout.good()) {
    std::cerr << "Output file is invalid." << std::endl;
    return -1;
  }

  Aws::SDKOptions options;
  Aws::InitAPI(options);
  {
    Aws::Translate::TranslateClient translate_client;
    Aws::Translate::Model::TranslateTextRequest request;
    request = request.WithSourceLanguageCode("auto").WithTargetLanguageCode(target_language);

    Aws::String line;
    while (getline(fin, line)) {
      if (line.empty()) {
        continue;
      }

      if (line.length() > MAX_LINE_LENGTH) {
        std::cerr << "Line is over " << MAX_LINE_LENGTH << " characters long." << std::endl;
        break;
      }

      request.SetText(line);
      auto outcome = translate_client.TranslateText(request);

      if (outcome.IsSuccess()) {
        auto translation = outcome.GetResult().GetTranslatedText();
        std::cout << translation << std::endl;
        fout << translation << std::endl;
      } else {
        std::cout << "TranslateText error: " << outcome.GetError().GetExceptionName()
             << " - " << outcome.GetError().GetMessage() << std::endl;
        break;
      }
    }
  }
  Aws::ShutdownAPI(options);
}
