# 1. Variable Name Independence
# Low-entropy placeholder values: Anthropic Credentials
X = "sk-ant-api03-abcdef1234567890abcdef1234567890abcdef123456"

# 2. URL Embedding
# SECRET: Openai Token Credentials
endpoint = "https://api.openai.com/v1/chat/completions?auth=sk-U8k2pLz9qR5sT7vX1yW3zB4nM6mQ8pLz9qR5sT7vX1yW"
# SECRET: Google Gemini Credentials
gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyAbCdEfGhIjKlMnOpQrStUvWxYz1234567"

# 3. Base64 Encoding (Common Obfuscation)
# This is "sk-ant-api03-abcdef1234567890abcdef1234567890abcdef123456" encoded in base64
# Low-entropy placeholder values: high-entropy-string
encoded_secret = "c2stYW50LWFwaTAzLWFiY2RlZjEyMzQ1Njc4OTBhYmNkZWYxMjM0NTY3ODkwYWJjZGVmMTIzNDU2"

