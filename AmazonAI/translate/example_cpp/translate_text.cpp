#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/translate/TranslateClient.h>
#include <aws/translate/model/TranslateTextRequest.h>
#include <aws/translate/model/TranslateTextResult.h>

int main(int argc, char **argv) {
  if (argc != 3) {
    std::cout
        << "Usage: translate_text 'target language code' 'text to translate'"
        << std::endl;
    return -1;
  }

  Aws::SDKOptions options;
  Aws::InitAPI(options);
  {
    Aws::Translate::TranslateClient translate_client;

    const Aws::String target_language = argv[1];
    const Aws::String text = argv[2];

    Aws::Translate::Model::TranslateTextRequest request;
    request = request.WithSourceLanguageCode("auto")
                  .WithTargetLanguageCode(target_language)
                  .WithText(text);

    auto outcome = translate_client.TranslateText(request);
    if (outcome.IsSuccess()) {
      std::cout << "The translated text is:" << std::endl;
      std::cout << outcome.GetResult().GetTranslatedText() << std::endl;
    } else {
      std::cout << "TranslateText error: "
                << outcome.GetError().GetExceptionName() << " - "
                << outcome.GetError().GetMessage() << std::endl;
    }
  }
  Aws::ShutdownAPI(options);
}
