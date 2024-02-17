import "@typespec/rest";
import "@typespec/http";

using TypeSpec.Http;
using TypeSpec.Rest;

@doc("A specific deployment")
@TypeSpec.Rest.resource("deployments")
model Deployment {
  @visibility("read")
  @doc("Specifies either the model deployment name (when using Azure OpenAI) or model name (when using non-Azure OpenAI) to use for this request.")
  @projectedName("java", "deploymentOrModelName")
  @key
  deploymentId: string;
}
