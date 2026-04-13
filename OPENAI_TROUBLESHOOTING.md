# 🔧 OpenAI Error Troubleshooting Guide

## Error: "Insufficient Quota" (Error Code 429)

### ❌ What This Means
Your OpenAI account has exhausted its available credits or quota. This is the **most common issue** and has several causes:

1. **Free trial credits expired** - $5 free credit lasts only 3 months
2. **No payment method added** - Account can't make API calls without billing setup
3. **Spending limit reached** - You set a quota and hit it
4. **Account flagged** - Unusual activity detected

---

## ✅ How to Fix It (5 Minutes)

### **Step 1: Check Your Account Status**
Go to: **https://platform.openai.com/account/billing/overview**

Look for:
- 🟢 **"Active plan"** = Good, problem is elsewhere
- 🔴 **"No active plan"** = Need to add payment method
- 🔴 **"Credits expired"** = Free trial ended, need paid plan
- 🔴 **"Quota exceeded"** = Hit your spending limit

### **Step 2: Add Payment Method (If Needed)**

**If you see "No active plan":**
1. Click **"Set up paid account"**
2. Click **"Add payment method"**
3. Enter credit card details
4. Click **"Save card"**
5. You're now on pay-as-you-go billing

**Pricing:** ~$0.001 per recipe chat (very cheap!)

### **Step 3: Get a Fresh API Key**

1. Go to: **https://platform.openai.com/api-keys**
2. Find your old key (should show as "Limited")
3. Click **the trash icon to DELETE it**
4. Click **"+ Create new secret key"**
5. Copy the key immediately (won't show again!)
6. Save it somewhere safe

### **Step 4: Update the App**

1. Open Recipe de SUCKERPUNCH app
2. In **sidebar**, select **"Delicious de Recipe (OpenAI)"**
3. Find **"OpenAI API Key"** field
4. **Paste your NEW key** (from Step 3)
5. See **✅ confirmation**
6. Try your recipe request again!

### **Step 5: Verify It Works**

Test with a simple request:
```
"I have chicken, garlic, and lemon. What should I make?"
```

Should get a response within 1-3 seconds!

---

## 🎯 All Error Messages & Solutions

### Error: "Insufficient Quota"
**Cause:** Free credits expired or no payment method  
**Solution:** Add payment method at https://platform.openai.com/account/billing/overview

### Error: "Invalid API Key"
**Cause:** Key is expired, deleted, or wrong  
**Solution:** Create new key at https://platform.openai.com/api-keys

### Error: "Authentication Failed"
**Cause:** API key not configured or incorrect  
**Solution:** Verify key in sidebar, create fresh key if needed

### Error: "Rate Limit Exceeded"
**Cause:** Too many requests in short time  
**Solution:** Wait a few minutes, then try again

### Error: "Model Not Found"
**Cause:** Account doesn't have access to gpt-3.5-turbo  
**Solution:** Check account status, may need different plan

---

## 💰 Understanding Costs

### Pricing Breakdown
- **Model:** GPT-3.5-Turbo
- **Input:** ~$0.0005 per 1K tokens
- **Output:** ~$0.0015 per 1K tokens
- **Average recipe chat:** ~500 total tokens = ~$0.001

### Example Costs
| Usage | Cost |
|-------|------|
| 10 recipe chats | ~$0.01 |
| 100 recipe chats | ~$0.10 |
| 1,000 recipe chats | ~$1.00 |
| Daily cooking help | ~$0.03/day |

### Track Your Usage
Visit: **https://platform.openai.com/account/usage/overview**
- See real-time usage
- Check current billing period
- Monitor remaining quota

### Set Spending Limits (Recommended)
1. Go to: https://platform.openai.com/account/billing/limits
2. Set **"Hard limit"** (e.g., $10/month)
3. API will stop working when limit reached
4. Prevents surprise bills

---

## 🚀 Quick Fixes (Try These First)

### Fix 1: Clear Browser Cache
1. Clear cookies for openai.com
2. Log back in
3. Check billing status again

### Fix 2: Generate New API Key
1. Go to: https://platform.openai.com/api-keys
2. Delete old key
3. Create new key
4. Paste new key in app
5. Try again

### Fix 3: Check Your Plan Type
1. Go to: https://platform.openai.com/account/billing/overview
2. Look at "Plan" section
3. If "Free trial", you need to upgrade:
   - Click "Set up paid account"
   - Add credit card
   - Confirm

### Fix 4: Verify Internet Connection
1. Check you have internet access
2. Try visiting: https://api.openai.com/
3. You should see "Unauthorized"

### Fix 5: Switch to Local Mode (Temporary)
While fixing OpenAI:
1. Select **"Recipe de SUCKERPUNCH (Local)"** in sidebar
2. Get instant free recipes
3. No API key needed
4. Switch back once OpenAI is fixed

---

## 🛠️ Advanced Troubleshooting

### Check API Key Format
Your key should:
- Start with `sk-`
- Be ~48 characters long
- Example: `sk-proj-abc123...xyz789`

If your key doesn't look right, generate a new one!

### Check Environment Variable (If Using)
If you're using `OPENAI_API_KEY` environment variable:

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY
# Should show your key, not empty
```

**macOS/Linux:**
```bash
echo $OPENAI_API_KEY
# Should show your key, not empty
```

If empty, set it:
```bash
export OPENAI_API_KEY="sk-..."
```

### Test API Directly
```python
from openai import OpenAI
client = OpenAI(api_key="sk-...")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

If this fails, problem is with OpenAI account, not the app.

---

## 📋 Checklist Before Contacting Support

- [ ] I added a payment method to my OpenAI account
- [ ] I created a new API key (within last 5 minutes)
- [ ] I pasted the exact new key in the app sidebar
- [ ] I clicked the ✅ confirmation in the sidebar
- [ ] I waited 1 minute for changes to take effect
- [ ] I tried with a simple request like "chicken recipe"
- [ ] I cleared my browser cache
- [ ] I checked https://platform.openai.com/account/usage/overview for usage

If all above are done and error persists, contact OpenAI support.

---

## 🆘 When to Contact OpenAI Support

Email: **support@openai.com**

Include:
1. Your OpenAI email
2. The error message (full text)
3. When it started happening
4. What you were trying to do
5. Screenshots of:
   - The error in your app
   - Your billing page
   - Your API keys page

---

## 💡 Preventing Future Issues

### 1. Set Spending Limit
- Go to: https://platform.openai.com/account/billing/limits
- Set "Hard limit" to $10/month
- API stops when limit reached
- No surprise bills!

### 2. Monitor Usage Weekly
- Check: https://platform.openai.com/account/usage/overview
- See your spending
- Plan ahead if approaching limit

### 3. Use Local Mode for Basic Requests
Switch to **Recipe de SUCKERPUNCH (Local)** for:
- Quick recipe ideas
- Simple substitutions
- Meal planning
- **Save API credits for complex requests!**

### 4. Keep API Key Safe
- ❌ Don't share with anyone
- ❌ Don't commit to GitHub
- ❌ Don't hardcode in scripts
- ✅ Use environment variables
- ✅ Regenerate if accidentally exposed

### 5. Test with Sidebar Before Coding
- Always test API setup in the app sidebar first
- Don't write code relying on API until you know it works
- Easier to debug in the UI

---

## 📞 Getting Help

### Option 1: Use Local Mode
Select **"Recipe de SUCKERPUNCH (Local)"** = Free instant responses

### Option 2: Contact OpenAI
- Billing issues: https://platform.openai.com/account/billing
- Account issues: support@openai.com
- API errors: Check docs at https://platform.openai.com/docs

### Option 3: Check This Guide
Reread this troubleshooting guide and follow the checklist

---

## ⚡ Quick Reference

| Problem | Solution | Time |
|---------|----------|------|
| Insufficient quota | Add payment method | 2 min |
| Invalid API key | Create new key | 1 min |
| No active plan | Add credit card | 3 min |
| Rate limited | Wait 5 min | 5 min |
| Not sure | Check billing page | 2 min |

---

## 📚 Useful Links

- **Billing Dashboard:** https://platform.openai.com/account/billing/overview
- **API Keys:** https://platform.openai.com/api-keys
- **Usage Statistics:** https://platform.openai.com/account/usage/overview
- **Spending Limits:** https://platform.openai.com/account/billing/limits
- **Documentation:** https://platform.openai.com/docs
- **Support:** support@openai.com

---

**Remember:** For immediate cooking help while fixing OpenAI, just switch to **Recipe de SUCKERPUNCH (Local)** mode! 🍳
