# 🚀 Quick Start Guide - Delicious de Recipe (OpenAI)

## 30-Second Setup

### Option 1: Environment Variable (Recommended)

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "sk-..."
streamlit run app.py
```

**macOS/Linux:**
```bash
export OPENAI_API_KEY="sk-..."
streamlit run app.py
```

### Option 2: In the App (Manual)

1. Select **"Delicious de Recipe (OpenAI)"** in sidebar
2. Paste your API key in **"OpenAI API Key"** field
3. See ✅ confirmation

---

## Get Your API Key

1. Go to: https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy & save it (one-time visibility)
4. You have $5 free credit (expires in 3 months)

---

## Try It Out

1. Run the app: `streamlit run app.py`
2. Select "Delicious de Recipe (OpenAI)" from sidebar
3. Enter your API key
4. Ask a cooking question:
   - "I have chicken, garlic, and lemon. What should I make?"
   - "How do I make crispy pan-seared salmon?"
   - "Vegan keto recipes with cashews?"

---

## Common Issues

| Issue | Solution |
|-------|----------|
| "API key not configured" | Paste your key in sidebar |
| "Error calling OpenAI" | Check API key, restart app |
| Slow responses | Normal latency, wait a moment |
| Out of free credit | Switch to Recipe de SUCKERPUNCH mode |

---

## Cost Estimate

- **Price:** ~$0.0003 - $0.001 per chat
- **Free credit:** ~5,000 chats
- **Track usage:** https://platform.openai.com/account/usage/overview

---

## Switch Back to Local Mode

Select **"Recipe de SUCKERPUNCH (Local)"** for instant, free responses.

---

For detailed info, see **OPENAI_INTEGRATION.md**
