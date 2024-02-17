import "@azure-tools/typespec-client-generator-core";

import "./client/custom_visibility.tsp";
import "./main.tsp";

using Azure.ClientGenerator.Core;

#suppress "@azure-tools/typespec-azure-core/casing-style" "OpenAI is a case-sensitive name"
@TypeSpec.Versioning.useDependency(
  Azure.OpenAI.ServiceApiVersions.v2023_12_01_Preview
)
namespace Client;

#suppress "@azure-tools/typespec-azure-core/casing-style" "OpenAI is a case-sensitive name"
@client({
  name: "OpenAIClient",
  service: Azure.OpenAI,
})
interface OpenAIClient {
  getCompletions is Azure.OpenAI.getCompletions;
  getChatCompletions is Azure.OpenAI.getChatCompletions;
  getChatCompletionsWithAzureExtensions is Azure.OpenAI.getChatCompletionsWithAzureExtensions;

  getImageGenerations is Azure.OpenAI.getImageGenerations;

  getEmbeddings is Azure.OpenAI.getEmbeddings;
}
