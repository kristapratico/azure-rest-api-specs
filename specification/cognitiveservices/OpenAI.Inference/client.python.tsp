import "@azure-tools/typespec-client-generator-core";
import "./main.tsp";
import "@typespec/versioning";

using TypeSpec.Versioning;

using Azure.ClientGenerator.Core;


@client({
  name: "OpenAIClient",
  service: Azure.OpenAI
})

@useDependency(Azure.OpenAI.ServiceApiVersions.v2023_09_01_Preview)
namespace Customizations;
@operationGroup
interface Completions{
  create is Azure.OpenAI.getCompletions
}

@@internal(Azure.OpenAI.getCompletions);

@operationGroup
interface ChatCompletions{
  create is Azure.OpenAI.getChatCompletions;
  createExtensions is Azure.OpenAI.getChatCompletionsWithAzureExtensions;
}

@@internal(Azure.OpenAI.getChatCompletions);
@@internal(Azure.OpenAI.getChatCompletionsWithAzureExtensions);

@operationGroup
interface Embeddings{
  create is Azure.OpenAI.getEmbeddings
}

@@internal(Azure.OpenAI.getEmbeddings);

@operationGroup
interface Images{
  generate is Azure.OpenAI.beginAzureBatchImageGeneration
}

@@internal(Azure.OpenAI.beginAzureBatchImageGeneration);

@operationGroup
interface Audio{
  transcriptions is Azure.OpenAI.getAudioTranscriptionAsResponseObject;
  translations is Azure.OpenAI.getAudioTranslationAsResponseObject;
}

@@internal(Azure.OpenAI.getAudioTranscriptionAsResponseObject);
@@internal(Azure.OpenAI.getAudioTranslationAsResponseObject);

// Azure-specific long-running operations should be treated as implementation details that are wrapped into
// appropriately merged public surface.
@@internal(Azure.OpenAI.beginAzureBatchImageGeneration);
@@internal(Azure.OpenAI.getAzureBatchImageGenerationOperationStatus);

// Azure-specific Chat Completions with extensions should be handled by clients as a conditional selection within the
// shared Chat Completions route, with the selection gated by the presence or non-presence of additional child
// configuration options on the request payload options model.
@@internal(Azure.OpenAI.getChatCompletionsWithAzureExtensions);

// Some models from routes with suppressed visibility are still desired for custom public surface.
@@include(Azure.OpenAI.ImageGenerationOptions);
@@include(Azure.OpenAI.ImageLocation);
@@include(Azure.OpenAI.ImageGenerations);
