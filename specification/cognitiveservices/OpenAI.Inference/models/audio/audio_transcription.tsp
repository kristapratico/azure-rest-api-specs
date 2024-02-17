import "@typespec/versioning";
import "./common.tsp";

namespace Azure.OpenAI;

using TypeSpec.Versioning;

@doc("Defines available options for the underlying response format of output transcription information.")
@added(ServiceApiVersions.v2023_09_01_Preview)
enum AudioTranscriptionFormat {
  @doc("Use a response body that is a JSON object containing a single 'text' field for the transcription.")
  json: "json",

  @doc("""
    Use a response body that is a JSON object containing transcription text along with timing, segments, and other
    metadata.
    """)
  verbose_json: "verbose_json",

  @doc("Use a response body that is plain text containing the raw, unannotated transcription.")
  text: "text",

  @doc("Use a response body that is plain text in SubRip (SRT) format that also includes timing information.")
  srt: "srt",

  @doc("""
    Use a response body that is plain text in Web Video Text Tracks (VTT) format that also includes timing information.
    """)
  vtt: "vtt",
}

@doc("""
The configuration information for an audio transcription request.
""")
@added(ServiceApiVersions.v2023_09_01_Preview)
model AudioTranscriptionOptions {
  @doc("""
  An optional hint to guide the model's style or continue from a prior audio segment. The written language of the
  prompt should match the primary spoken language of the audio data.
  """)
  prompt?: string;
}

@doc("""
Extended information about a single segment of transcribed audio data.
Segments generally represent roughly 5-10 seconds of speech. Segment boundaries typically occur between words but not
necessarily sentences.
""")
@added(ServiceApiVersions.v2023_09_01_Preview)
model AudioTranscriptionSegment {
  @doc("The transcribed text that was part of this audio segment.")
  text: string;

}

@doc("Result information for an operation that transcribed spoken audio into written text.")
@added(ServiceApiVersions.v2023_09_01_Preview)
model AudioTranscription {
  @doc("The transcribed text for the provided audio data.")
  text: string;
}
