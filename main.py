# main.py
# This script demonstrates a system for generating rich, descriptive narratives
# from simplified 3D scene data using an LLM, simulating the GPT-4 Vision API's
# contextual understanding for spatial platforms.

import json

# In a real application, you would use the OpenAI client library.
# from openai import OpenAI
# client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# --- 1. Simplified 3D Scene Data ---
# This data structure represents a scene that would be extracted from a
# platform like Three.js or Blender. It includes objects with tags,
# materials, and positions to give the AI spatial context.

scene_data = {
    "scene_name": "Modern Loft Living Room",
    "overall_style": "Minimalist, Industrial",
    "lighting": {
        "type": "Natural, bright afternoon sun",
        "source": "Large floor-to-ceiling windows"
    },
    "objects": [
        {
            "id": "sofa_01",
            "name": "Leather Sofa",
            "tags": ["seating", "main furniture", "comfortable"],
            "material": "Distressed brown leather",
            "position": "Center of the room, facing the windows"
        },
        {
            "id": "table_01",
            "name": "Concrete Coffee Table",
            "tags": ["table", "centerpiece", "functional"],
            "material": "Polished concrete with steel legs",
            "position": "In front of the leather sofa"
        },
        {
            "id": "plant_01",
            "name": "Fiddle Leaf Fig",
            "tags": ["plant", "organic", "decoration", "life"],
            "material": "Green leaves, terracotta pot",
            "position": "In the corner, near the windows"
        },
        {
            "id": "lamp_01",
            "name": "Arc Floor Lamp",
            "tags": ["lighting", "modern", "accent"],
            "material": "Brushed nickel",
            "position": "Arching over the sofa from behind"
        },
        {
            "id": "art_01",
            "name": "Abstract Painting",
            "tags": ["art", "wall decor", "color accent"],
            "material": "Canvas with bold blue and yellow strokes",
            "position": "On the exposed brick wall behind the sofa"
        }
    ]
}

# --- 2. Complex Prompt Chain Engineering ---
# This is the core of the project. We create a detailed, multi-part prompt
# that instructs the LLM to act as a specific persona (a virtual curator)
# and provides a structured format for its output.

def create_curator_prompt(scene):
    """
    Constructs a complex prompt to guide the LLM in generating a rich,
    contextually aware narrative for the 3D scene.
    """
    
    # Convert the object list into a more readable format for the prompt
    object_descriptions = "\n".join([
        f"- {obj['name']}: Made of {obj['material']}. Positioned at: {obj['position']}. Tags: {', '.join(obj['tags'])}."
        for obj in scene['objects']
    ])

    prompt = f"""
    **Persona Instruction:**
    You are an expert virtual curator and interior design storyteller for a high-end spatial computing platform. Your task is to transform raw 3D scene data into a rich, evocative, and engaging narrative. Do not just list the objects. Instead, weave them into a cohesive story that describes the atmosphere, the lifestyle of the imagined owner, and the interplay between the elements.

    **Contextual Scene Data:**
    - Scene Name: {scene['scene_name']}
    - Dominant Style: {scene['overall_style']}
    - Lighting Conditions: {scene['lighting']['type']} from {scene['lighting']['source']}
    - Objects in Scene:
    {object_descriptions}

    **Task & Output Structure:**
    Based on the data above, generate a JSON object with three distinct keys: "title", "narrative", and "design_suggestions".

    1.  **title**: Create a short, catchy, and descriptive title for this scene.
    2.  **narrative**: Write a detailed, multi-paragraph story about the space.
        - Start by describing the overall feeling and atmosphere created by the lighting and style.
        - Describe how the main furniture pieces (like the sofa and table) anchor the space.
        - Integrate the decorative elements (plant, art) into the narrative, explaining how they contribute to the mood.
        - Imply the personality of the person who lives here through your description.
    3.  **design_suggestions**: Provide three actionable design suggestions as a list of strings. These should be creative ideas to enhance the space further, based on the existing elements. For example, suggest adding a complementary texture, a specific type of rug, or another piece of decor.

    **Constraint:**
    Your final output must be a single, valid JSON object and nothing else. Do not include any explanatory text before or after the JSON.
    """
    return prompt

# --- 3. LLM API Call Simulation ---

async def generate_scene_content(scene_data):
    """
    Simulates making a call to an LLM API (like GPT-4) with the engineered prompt.
    """
    prompt = create_curator_prompt(scene_data)
    print("--- Generated Prompt for LLM ---")
    print(prompt)
    print("---------------------------------")
    
    # In a real application, this is where the API call would be made.
    # response = client.chat.completions.create(
    #     model="gpt-4-turbo",
    #     messages=[{"role": "user", "content": prompt}],
    #     response_format={"type": "json_object"}
    # )
    # return response.choices[0].message.content

    # For this demonstration, we will return a mock JSON response that
    # mimics the expected output from the LLM.
    mock_response = {
        "title": "Sun-Drenched Industrial Serenity",
        "narrative": "As the bright afternoon sun streams through vast, floor-to-ceiling windows, it illuminates a space that is both raw and refined. This modern loft is a sanctuary of minimalist industrial design, where every object feels intentional. The centerpiece is a handsome, distressed brown leather sofa, its worn texture inviting you to sink in and relax. It faces the light, suggesting a resident who appreciates warmth and openness.\n\nIn front of it, a polished concrete coffee table stands as a testament to functional art, its cool surface and steel legs providing a stark, beautiful contrast to the sofa's warmth. Life is breathed into the space by a tall Fiddle Leaf Fig, its vibrant green leaves reaching for the sun from a terracotta pot in the corner. Above, a brushed nickel arc lamp elegantly sweeps over the seating area, ready to provide a focused glow as day turns to night. The entire scene is anchored by a bold, abstract painting on the exposed brick wall, its energetic blue and yellow strokes infusing the calm space with a burst of creative spirit. This is clearly the home of a discerning individual with an eye for design and a love for uncluttered, light-filled living.",
        "design_suggestions": [
            "Add a soft, high-pile wool rug in a neutral grey or cream color under the sofa and coffee table to soften the concrete and add textural warmth.",
            "Introduce a set of floating wooden shelves on the brick wall to display books or curated objects, adding a personal touch.",
            "Consider adding a single, comfortable armchair in a contrasting fabric like dark blue velvet to create a cozy reading nook."
        ]
    }
    
    return json.dumps(mock_response, indent=2)


# --- 4. Main Execution ---
if __name__ == "__main__":
    print("Generating 3D-aware content for the scene...")
    generated_content_json = await generate_scene_content(scene_data)
    
    print("\n--- Generated Content (JSON Output) ---")
    print(generated_content_json)
    print("--------------------------------------")

    # You can now parse and use this structured data in your application
    content_obj = json.loads(generated_content_json)
    print(f"\nTitle: {content_obj['title']}")

