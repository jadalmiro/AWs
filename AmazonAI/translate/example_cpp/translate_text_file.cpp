#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/translate/TranslateClient.h>
#include <aws/translate/model/TranslateTextRequest.h>
#include <aws/translate/model/TranslateTextResult.h>

#include <fstream>
#include <iostream>
#include <string>

const int MAX_LINE_LENGTH=5000;

int main(int argc, char **argv) {
  if (argc != 4) {
    std::cout << "Usage: translate_text_file 'target language code' 'input file'"
            "'output file'"
         << std::endl;
    return -1;
  }

  std::ifstream fin(argv[2], std::ios::in);
  if (!fin.good()) {
    std::cerr << "Input file is invalid." << std::endl;
    return -1;
  }

  std::ofstream fout(argv[3], std::ios::out);
  if (!fout.good()) {
    std::cerr << "Output file is invalid." << std::endl;
    return -1;
  }

  Aws::SDKOptions options;
  Aws::InitAPI(options);
  {
    const Aws::Translate::TranslateClient translate_client;

    Aws::Translate::Model::TranslateTextRequest request;
    request = request.WithSourceLanguageCode("auto").WithTargetLanguageCode(argv[1]);

    Aws::String line;
    while (getline(fin, line)) {
      if (line.empty()) {
        continue;
      }

      if (line.length() > MAX_LINE_LENGTH) {
        std::cerr << "Line is too long." << std::endl;
        break;
      }

      request.SetText(line);

      auto outcome = translate_client.TranslateText(request);
      if (outcome.IsSuccess()) {
        fout << outcome.GetResult().GetTranslatedText() << std::endl;
      } else {
        auto error = outcome.GetError();
        std::cout << "TranslateText error: " << error.GetExceptionName()
             << " - " << error.GetMessage() << std::endl;
        break;
      }
    }
  }
  Aws::ShutdownAPI(options);
}
