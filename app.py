import streamlit as st
import random

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Cook de Staku - AI Recipe Generator",
    page_icon="🍳",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#ff6a00,#ff8c00,#ffb300,#ffd54f);
background-attachment: fixed;
font-family: 'Segoe UI', sans-serif;
color:#1a1a1a;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
background: linear-gradient(180deg,#ff8c00,#ffb300);
color:white;
font-weight:bold;
}

/* TITLES */
h1{
color:#3a0ca3;
font-weight:900;
font-size:3rem;
text-shadow: 1px 1px 2px #ffb300;
}

h2,h3{
color:#3a0ca3;
font-weight:800;
text-shadow: 1px 1px 1px #ffa500;
}

/* BUTTON STYLE */
.stButton>button{
background: linear-gradient(90deg,#f77f00,#ffb300);
color:white;
border-radius:15px;
border:none;
height:3.2em;
font-weight:bold;
font-size:1.1rem;
transition:0.3s;
box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}

.stButton>button:hover{
background: linear-gradient(90deg,#ff6a00,#ffb300);
transform:scale(1.05);
}

/* INPUT BOX */
.stTextInput>div>div>input{
border-radius:12px;
border:2px solid #ff8c00;
padding:8px;
font-size:1rem;
}

/* RECIPE CARD */
.recipe-card{
background: rgba(255,255,255,0.95);
padding:25px;
border-radius:20px;
box-shadow: 0px 10px 25px rgba(0,0,0,0.25);
margin-top:20px;
transition: 0.3s;
}

.recipe-card:hover{
transform: scale(1.02);
}

/* USER CHAT BOX */
.chatbox{
background:white;
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
font-size:1rem;
}

/* AI CHAT BOX */
.botbox{
background:#fff3cd;
padding:18px;
border-radius:15px;
margin-top:10px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
font-size:1rem;
}

/* CHAT MESSAGE */
.stChatMessage>div{
border-radius:15px;
}

/* INPUT BOX HIGHLIGHT */
.stTextInput>div>div>input:focus{
border:2px solid #ff6a00;
box-shadow:0 0 8px #ffa500;
}

/* HORIZONTAL RULE */
hr{
border-top: 2px solid #ff8c00;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.title("🍳 Cook de Staku")
st.subheader("Smart Recipe Coach for Modern Home Cooks")

# -------------------------
# NAVIGATION
# -------------------------
st.write("### 🍽 Select Cook de Staku Mode")
col1, col2, col3 = st.columns(3)

if "mode" not in st.session_state:
    st.session_state.mode = "Generate Recipe"

with col1:
    if st.button("🍳 Recipe Generator"):
        st.session_state.mode = "Generate Recipe"

with col2:
    if st.button("🔄 Ingredient Substitute"):
        st.session_state.mode = "Ingredient Substitute"

with col3:
    if st.button("📅 Meal Planner"):
        st.session_state.mode = "Meal Planner"

mode = st.session_state.mode

# -------------------------
# SIDEBAR SETTINGS
# -------------------------
st.sidebar.title("⚙ Cooking Settings")

skill_level = st.sidebar.select_slider(
    "Cooking Skill Level",
    ["Beginner", "Intermediate", "Advanced"]
)

servings = st.sidebar.number_input("Serving Size", 1, 10, 2)

diet = st.sidebar.multiselect(
    "Dietary Preference",
    ["Vegan", "Vegetarian", "Keto", "Gluten Free"]
)

st.sidebar.write("---")
st.sidebar.write("👨‍🍳 Team Summer Daze Members")
st.sidebar.write("👤 Nikolai Javier Jr.")
st.sidebar.write("👤 Claudine Margaret Ricablanca")
st.sidebar.write("👤 Gwyn Sapio")

st.sidebar.write("---")
st.sidebar.write("👨‍🍳 ChefDaze AI Response Team by (BINI x All Time Low)")
st.sidebar.write("👤💙 Jhoanna")
st.sidebar.write("👤💚 Colet")
st.sidebar.write("👤💛 Maloi")
st.sidebar.write("👤❤️ Mikha")
st.sidebar.write("👤🩷 Stacey")
st.sidebar.write("👤🩵 Aiah")
st.sidebar.write("👤🧡 Gwen")
st.sidebar.write("👤💜 Sheena")
st.sidebar.write("👤🤍 Alex Gaskarth")
st.sidebar.write("👤🩶 Jack Barakat")
st.sidebar.write("👤🖤 Zack Merrick")
st.sidebar.write("👤🤎 Rian Dawson")

# -------------------------
# SMART AI RECIPE FUNCTION
# -------------------------
def generate_recipe(ingredients):
    ingredients = ingredients.lower()
    base = f"### 🥗 Smart Recipe for: {ingredients.title()}\n\nServing Size: {servings}\n"

    # Default Prep & Cook Time
    prep = "Prep Time: 10 mins"
    cook = "Cook Time: 20 mins"

    ingredient_list = []
    instructions = []

    # Chicken-based
    if "chicken" in ingredients:
        ingredient_list += ["Chicken", "Garlic", "Soy Sauce", "Cooking Oil", "Pepper"]
        instructions += [
            "Heat oil in a pan.",
            "Sauté garlic until fragrant.",
            "Add chicken and cook until browned.",
            "Pour soy sauce and simmer.",
            "Serve hot with rice or noodles."
        ]
    # Pasta-based
    if "pasta" in ingredients or "spaghetti" in ingredients:
        ingredient_list += ["Pasta", "Butter", "Garlic", "Parmesan Cheese", "Olive Oil"]
        instructions += [
            "Boil pasta until al dente.",
            "Melt butter in a pan.",
            "Add minced garlic and olive oil.",
            "Toss pasta with sauce.",
            "Sprinkle parmesan and serve."
        ]
    # Vegetable-based
    if any(x in ingredients for x in ["vegetable", "broccoli", "carrot", "spinach"]):
        ingredient_list += ["Mixed Vegetables", "Garlic", "Soy Sauce", "Olive Oil"]
        instructions += [
            "Heat oil in a pan.",
            "Add vegetables and sauté for 5-7 minutes.",
            "Add soy sauce and toss.",
            "Serve hot as side dish or main."
        ]
    # Other common ingredients
    if "rice" in ingredients:
        ingredient_list.append("Rice")
    if "egg" in ingredients:
        ingredient_list.append("Eggs")

    # Remove duplicates
    ingredient_list = list(dict.fromkeys(ingredient_list))

    # Format output
    ingredients_text = "\n".join(f"- {i}" for i in ingredient_list)
    instructions_text = "\n".join(f"{idx+1}. {step}" for idx, step in enumerate(instructions))

    return f"""
{base}
{prep}  
{cook}  

**Ingredients**  
{ingredients_text}

**Instructions**  
{instructions_text}
"""

# -------------------------
# Ingredient Substitute
# -------------------------
def substitute_ingredient(question):
    question = question.lower()
    subs = {
        "egg": ["1/4 cup applesauce", "1 mashed banana", "1 tbsp flaxseed + 3 tbsp water", "Yogurt"],
        "milk": ["Almond milk", "Soy milk", "Oat milk", "Coconut milk"],
        "butter": ["Margarine", "Olive oil", "Coconut oil", "Avocado"],
        "sugar": ["Honey", "Maple syrup", "Agave nectar"],
        "flour": ["Oat flour", "Almond flour", "Coconut flour"]
    }
    for key, value in subs.items():
        if key in question:
            return f"🥚 {key.title()} Substitutes\n\n- " + "\n- ".join(value)
    return "Try specifying which ingredient you want to substitute."

# -------------------------
# Weekly Meal Plan
# -------------------------
def meal_plan():
    return """
📅 Simple Weekly Meal Plan

Monday – Chicken Stir Fry  
Tuesday – Garlic Butter Pasta  
Wednesday – Fried Rice  
Thursday – Grilled Chicken Salad  
Friday – Vegetable Stir Fry  
Saturday – Homemade Pizza  
Sunday – Soup and Sandwich
"""

# -------------------------
# Recipe Image
# -------------------------
def get_recipe_image(recipe_name):
    images = {
        "chicken": "https://images.unsplash.com/photo-1604908177522-040cbe7c5a67",
        "pasta": "https://images.unsplash.com/photo-1551183053-bf91a1d81141",
        "stir fry": "https://images.unsplash.com/photo-1604908177261-8f3ec5d5b3c2",
        "salad": "https://images.unsplash.com/photo-1546069901-ba9599a7e63"
    }
    for key in images:
        if key in recipe_name.lower():
            return images[key]
    return "https://images.unsplash.com/photo-1495195134817-aeb325a55b65"

# -------------------------
# Nutrition Calculator
# -------------------------
def nutrition_estimate(ingredients):
    ingredients = ingredients.lower()
    calories = 0
    protein = 0
    if "chicken" in ingredients: calories += 250; protein += 30
    if "pasta" in ingredients: calories += 200; protein += 7
    if "rice" in ingredients: calories += 180
    if "butter" in ingredients: calories += 100
    if "garlic" in ingredients: calories += 5
    return f"""
🥗 Estimated Nutrition (per serving)

Calories: {calories} kcal  
Protein: {protein} g  
Carbohydrates: ~30 g  
Fat: ~10 g
"""

# -------------------------
# Grocery List
# -------------------------
def grocery_list(ingredients):
    items = ingredients.split(",")
    grocery = "\n".join([f"- {item.strip().title()}" for item in items if item])
    return f"""
🛒 Grocery List

{grocery}

Tip: Check your pantry before shopping!
"""

# -------------------------
# MAIN CONTENT
# -------------------------
if mode == "Generate Recipe":
    st.write("## 🧾 Enter Ingredients")
    ingredients = st.text_input("Example: chicken, garlic, rice, broccoli")
    if st.button("Generate Recipe"):
        recipe = generate_recipe(ingredients)
        image = get_recipe_image(ingredients)
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        st.image(image, use_container_width=True, caption="🍽 Your Dish Preview")
        st.markdown(recipe)
        st.markdown(nutrition_estimate(ingredients))
        st.markdown(grocery_list(ingredients))
        st.markdown('</div>', unsafe_allow_html=True)
        st.success("Recipe generated by Cook de Staku!")

elif mode == "Ingredient Substitute":
    st.write("## 🔄 Ingredient Substitute")
    question = st.text_input("Example: What can I use instead of eggs?")
    if st.button("Find Substitute"):
        response = substitute_ingredient(question)
        st.markdown('<div class="botbox">', unsafe_allow_html=True)
        st.write("👨‍🍳 Cook de Staku AI:")
        st.write(response)
        st.markdown('</div>', unsafe_allow_html=True)

elif mode == "Meal Planner":
    st.write("## 📅 Weekly Meal Planner")
    if st.button("Generate Meal Plan"):
        plan = meal_plan()
        st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
        st.write(plan)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# ChatGPT-Style Chat Interface with 12 Personas
# -------------------------
st.write("---")
st.write("## 💬 Chat with ChefDaze AI")

personas = {
    "Jhoanna": "💙",
    "Colet": "💚",
    "Maloi": "💛",
    "Mikha": "❤️",
    "Stacey": "🩷",
    "Aiah": "🩵",
    "Gwen": "🧡",
    "Sheena": "💜",
    "Alex": "🤍",
    "Jack": "🩶",
    "Zack": "🖤",
    "Rian": "🤎"
}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_chat = st.chat_input("Ask anything about cooking or recipes...")

if user_chat:
    st.session_state.chat_history.append(("user", user_chat))
    
    persona_name, persona_icon = random.choice(list(personas.items()))
    
    if "substitute" in user_chat.lower():
        response = substitute_ingredient(user_chat)
    elif "meal plan" in user_chat.lower():
        response = meal_plan()
    else:
        response = generate_recipe(user_chat)
    
    st.session_state.chat_history.append(("assistant", persona_name, persona_icon, response))

for message in st.session_state.chat_history:
    if message[0] == "user":
        with st.chat_message("user"):
            st.write(message[1])
    else:
        _, persona_name, persona_icon, text = message
        with st.chat_message("assistant"):
            st.markdown(f"**{persona_icon} {persona_name}:** {text}")