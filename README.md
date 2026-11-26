# Shimmie2 GraphQL Uploader

This Python script allows you to upload images to a Shimmie2 booru instance using its GraphQL API. (test)

Any other API method does not work and/or is undocumented.

I had to snoop into the source code myself to check this.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Setup

1.  **Clone or download** the `upload.py` script.
2.  **Edit `upload.py`**:
    *   Set `SHIMMIE_URL` to the base URL of your Shimmie2 instance (e.g., `http://my-booru-url`).
    *   Set `USERNAME` to your Shimmie2 username.
    *   Set `API_KEY` to your Shimmie2 API key.
        *   **Important**: This is *not* your password. You need to enable "User's API Keys" in your Shimmie2 board configuration. After enabling, your API key will be displayed at the bottom of your user profile page.

## Usage

Run the script from your terminal:

upload.py <file_path> -t "tag1 tag2 tag3" [-s "source_url"]

Arguments:

*   `<file_path>`: The path to the image file you want to upload.
*   `-t` or `--tags`: (Required) A space-separated string of tags to apply to the image. Enclose in quotes if it contains spaces.
*   `-s` or `--source`: (Optional) The source URL for the image. Enclose in quotes if it contains spaces.

### Examples:

1.  **Upload an image with tags:**

    upload.py my_image.jpg -t "original character cute"

2.  **Upload an image with tags and a source URL:**

    upload.py fanart.png -t "touhou reimu" -s "https://pixiv.net/artworks/12345678"

3. **Integration with Imgbrd-grabber**

    python upload.py "%path:nobackslash%" -t "%all:underscores,unsafe,separator= %"

## Troubleshooting

*   **"Error: File not found"**: Double-check the path to your image file.
*   **"Error: Please update 'USERNAME' and 'API_KEY'..."**: Make sure you've configured `USERNAME` and `API_KEY` in `upload.py`.
*   **"Upload failed: 403 Forbidden"**: Your API key might be incorrect, or the user associated with the API key doesn't have permission to upload.
*   **"Error: Received 200 OK, but response was NOT valid JSON."**: This often indicates a PHP error or warning was printed on the server before the JSON output. Check the "FULL RAW RESPONSE TEXT" in the output for clues.
*   **Network Errors**: Ensure your `SHIMMIE_URL` is correct and your machine has network access to the Shimmie2 instance.
