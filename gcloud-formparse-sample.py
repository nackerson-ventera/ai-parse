from google.cloud import documentai_v1 as documentai


def process_document(project_id: str, location: str,
                     processor_id: str, file_path: str,
                     mime_type: str) -> documentai.Document:
    """
    Processes a document using the Document AI API.
    """

    # Instantiates a client
    documentai_client = documentai.DocumentProcessorServiceClient()

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    resource_name = documentai_client.processor_path(
        project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

        # Load Binary Data into Document AI RawDocument Object
        raw_document = documentai.RawDocument(
            content=image_content, mime_type=mime_type)

        # Configure the process request
        request = documentai.ProcessRequest(
            name=resource_name, raw_document=raw_document)

        # Use the Document AI client to process the sample form
        result = documentai_client.process_document(request=request)

        return result.document


def main():
    """
    Run the project.
    """
    project_id = 'ventera-mockc-eat'
    location = 'us'  # Format is 'us' or 'eu'
    processor_id = 'a9db7f7e14e3f991'  # Create processor in Cloud Console

    # Supported File Types
    # https://cloud.google.com/document-ai/docs/processors-list#processor_form-parser
    file_path = 'assets/Invoice_Parser_HAiV.pdf'  # The local file in your current working directory
    mime_type = 'application/pdf'

    document = process_document(project_id=project_id, location=location,
                                processor_id=processor_id, file_path=file_path,
                                mime_type=mime_type)
    print("Document processing complete.")

    print(f"Text: {document.text}")
