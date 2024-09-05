# Unleash your Imagination: Craft compelling narratives from your Images using the magic of Gemini 1.5 Flash.

### Project Explanation:

This project harnesses the power of **Gemini 1.5 Flash**, Google's advanced large language model, to **analyze images and generate insightful information based on user prompts**. It works by:

- **Image Input:** The user provides an image, which the project processes to extract relevant features and data.
- **Prompt Input:** The user also supplies a prompt, guiding the type of information they want to generate from the image (e.g., "Describe the scene," "Identify objects," or "Write a creative story").
- **Gemini 1.5 Flash Integration:** The processed image data and prompt are fed into Gemini 1.5 Flash, which uses its powerful understanding of language and context to produce the desired information.
- **Output:** The generated information is presented to the user, offering insights, descriptions, or creative content based on the image and prompt.

### Potential Applications:
- **Image Captioning:** Automatically generate descriptive captions for images.
- **Object Recognition:** Identify and label objects within images.
- **Scene Understanding:** Provide detailed descriptions of the scene depicted in an image.
- **Creative Writing:** Generate stories, poems, or other creative content inspired by images.
- **Accessibility:** Help visually impaired users understand the content of images.

[click here](https://image2txt.streamlit.app) to view the Application.

https://github.com/user-attachments/assets/c1186827-dfd0-4b17-83f7-5d74d62c11f0

## How it Works
**1. Environment Setup:**

- The GOOGLE-API-KEY environment variable needs to be set with your valid Gemini API key.
- Necessary libraries are imported: **streamlit**, **google.generativeai**, **os**, **textwrap**, **PIL (Pillow)**, and pathlib.

**2. Streamlit App Initialization:**

- Sets the page title to "Gemini".
- Creates a header with the title "Gemini Image to Text Application 🖼️ 🖥️ 📄".

**3. User Input:**

- A text input field is provided for the user to enter a prompt (optional).
- A file uploader allows the user to upload an image.
- If an image is uploaded, it is displayed in the app.

**4. Gemini Interaction:**

- The **get_gemini_response** function handles the communication with the Gemini 1.5 Flash model.
- It takes the user's prompt and the uploaded image as input.
- If a prompt is provided, it is included in the request to Gemini along with the image otherwise, only the image is sent to Gemini.
- The generated text response from Gemini is returned.

**5. Output Presentation:**

When the "Do the Magic" button is clicked:
- The **get_gemini_response** function is called to generate the text.
- The generated text is displayed under the subheader "The Response is".
