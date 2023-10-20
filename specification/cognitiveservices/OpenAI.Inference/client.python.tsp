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

@@access(Azure.OpenAI.getCompletions, Access.internal);
@@access(Azure.OpenAI.Completions, Access.public);


@operationGroup
interface Chat{
  create is Azure.OpenAI.getChatCompletions;
  createExtensions is Azure.OpenAI.getChatCompletionsWithAzureExtensions;
}

@@access(Azure.OpenAI.getChatCompletions, Access.internal);
@@access(Azure.OpenAI.getChatCompletionsWithAzureExtensions, Access.internal);
@@access(Azure.OpenAI.ChatCompletions, Access.public);
@@access(Azure.OpenAI.ChatMessage, Access.public);
@@access(Azure.OpenAI.ChatChoice, Access.public);
@@access(Azure.OpenAI.Choice, Access.public);
@@access(Azure.OpenAI.ContentFilterResults, Access.public);
@@access(Azure.OpenAI.ContentFilterResult, Access.public);
@@access(Azure.OpenAI.PromptFilterResult, Access.public);
@@access(Azure.OpenAI.CompletionsUsage, Access.public);
@@access(Azure.OpenAI.FunctionDefinition, Access.public);
@@access(Azure.OpenAI.FunctionCall, Access.public);
@@access(Azure.OpenAI.AzureChatExtensionConfiguration, Access.public);
@@access(Azure.OpenAI.AzureChatExtensionsMessageContext, Access.public);
@@access(Azure.OpenAI.AzureChatExtensionType, Access.public);
@@access(Azure.OpenAI.ChatRole, Access.public);
@@access(Azure.OpenAI.ContentFilterSeverity, Access.public);
@@access(Azure.Core.Foundations.Error, Access.public);
@@usage(Azure.Core.Foundations.Error, Usage.output);

@operationGroup
interface Embeddings{
  create is Azure.OpenAI.getEmbeddings
}

@@access(Azure.OpenAI.getEmbeddings, Access.internal);
@@access(Azure.OpenAI.Embeddings, Access.public);
@@access(Azure.OpenAI.EmbeddingItem, Access.public);
@@access(Azure.OpenAI.EmbeddingsUsage, Access.public);

@operationGroup
interface Images{
  generate is Azure.OpenAI.beginAzureBatchImageGeneration
}

@@access(Azure.OpenAI.beginAzureBatchImageGeneration, Access.internal);
@@access(Azure.OpenAI.getAzureBatchImageGenerationOperationStatus, Access.internal);
@@access(Azure.OpenAI.ImageGenerations, Access.public);
@@access(Azure.OpenAI.ImageGenerationResponseFormat, Access.public);
@@access(Azure.OpenAI.ImageSize, Access.public);

@operationGroup
interface Audio{
  transcriptions is Azure.OpenAI.getAudioTranscriptionAsResponseObject;
  translations is Azure.OpenAI.getAudioTranslationAsResponseObject;
  transcriptionsText is Azure.OpenAI.getAudioTranscriptionAsPlainText;
  translationsText is Azure.OpenAI.getAudioTranslationAsPlainText;
}

@@access(Azure.OpenAI.getAudioTranscriptionAsResponseObject, Access.internal);
@@access(Azure.OpenAI.getAudioTranslationAsResponseObject, Access.internal);
@@access(Azure.OpenAI.getAudioTranscriptionAsPlainText, Access.internal);
@@access(Azure.OpenAI.getAudioTranslationAsPlainText, Access.internal);
@@access(Azure.OpenAI.AudioTranscription, Access.public);
@@access(Azure.OpenAI.AudioTranscriptionSegment, Access.public);
@@access(Azure.OpenAI.AudioTranslation, Access.public);
@@access(Azure.OpenAI.AudioTranslationSegment, Access.public);
@@access(Azure.OpenAI.AudioTaskLabel, Access.public);
@@access(Azure.OpenAI.AudioTranscriptionFormat, Access.public);
@@access(Azure.OpenAI.AudioTranslationFormat, Access.public);
