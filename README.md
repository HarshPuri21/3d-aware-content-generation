# 3D-Aware Content Generation for Spatial Platforms

This project demonstrates an advanced system for bridging the gap between raw 3D spatial data and rich, human-like creative storytelling. It uses a Large Language Model (LLM), simulating the contextual understanding of a multimodal model like GPT-4 Vision, to generate descriptive narratives and design suggestions for 3D scenes.

This work is directly aligned with the mission of building next-generation, AI-powered experiences for spatial computing platforms.

---

## Core Concept & Methodology

The central challenge in spatial computing is making digital environments feel immersive and meaningful. This project tackles that challenge by transforming a simple list of 3D objects and their properties into a cohesive and evocative story.

### 1. Simplified Scene Data
The system starts with a simplified, JSON-like representation of a 3D scene. This data, which could be programmatically extracted from platforms like **Three.js** or **Blender**, includes:
-   Object names and tags (e.g., "sofa", "seating").
-   Material descriptions (e.g., "distressed brown leather").
-   Positional information (e.g., "center of the room").
-   Overall scene metadata (e.g., lighting, style).

### 2. Complex Prompt Chaining
The key innovation of this project lies in the **prompt engineering**. A multi-part prompt chain is constructed to instruct the LLM to act as a specific persona—a "virtual curator" or "interior design storyteller." This prompt provides:
-   **Persona Instructions:** Defines the AI's role, tone, and objective.
-   **Contextual Data:** The structured 3D scene data is formatted and fed to the model.
-   **Structured Output:** The model is explicitly instructed to return its response in a clean, predictable JSON format with specific keys (`title`, `narrative`, `design_suggestions`). This makes the output reliable and easy to integrate into a frontend application.

### 3. From Data to Story
By combining a detailed persona with structured data and output requirements, the system guides the LLM to perform a creative leap. It doesn't just list the objects; it synthesizes the information to infer a story, a mood, and the personality of the imagined inhabitant of the space.

---

## Project Structure

-   `main.py`: A Python script that simulates the entire end-to-end process.
    -   Defines the sample 3D scene data.
    -   Contains the `create_curator_prompt` function, which is the core of the prompt engineering.
    -   Includes the `generate_scene_content` function, which simulates a call to an LLM API and returns a structured JSON object.
    -   The main execution block runs the process and prints the final, formatted output.

---

## How to Run

1.  **Prerequisites:**
    -   A Python 3.7+ environment.
    -   (For a real implementation) An OpenAI API key and the `openai` library (`pip install openai`).

2.  **Run the script:**
    ```bash
    python main.py
    ```

3.  **Output:**
    The script will first print the complex, multi-part prompt that it generates. It will then print the final, structured JSON output containing the AI-generated title, narrative, and design suggestions for the 3D scene.

