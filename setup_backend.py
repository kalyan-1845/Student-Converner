import os
import json

base_dir = r'C:\Users\prsnl\.gemini\antigravity\brain\d1b69639-1940-4d3a-9d7d-b4963cb4837c'

# 1. Create package.json for Vercel KV
package_json = {
  "name": "iic-certificate-portal",
  "version": "1.0.0",
  "dependencies": {
    "@vercel/kv": "^1.0.1"
  }
}
with open(os.path.join(base_dir, 'package.json'), 'w') as f:
    json.dump(package_json, f, indent=2)

# 2. Create api directory and serverless function
api_dir = os.path.join(base_dir, 'api')
os.makedirs(api_dir, exist_ok=True)

api_code = '''import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  try {
    // Increment the global counter in Vercel KV
    const newCount = await kv.incr('iic_cert_counter');
    
    // Hard cap at 70 certificates
    if (newCount > 70) {
      return res.status(400).json({ error: 'Registration closed. All 70 certificates have been claimed.' });
    }
    
    // Format to 3 digits (e.g., 001, 002)
    const formattedNumber = String(newCount).padStart(3, '0');
    const certId = ACE/IIC/2025-26/;
    
    return res.status(200).json({ certId, count: newCount });
  } catch (error) {
    return res.status(500).json({ error: 'Database connection error. Please ensure Vercel KV is linked in the Vercel Dashboard.' });
  }
}
'''
with open(os.path.join(api_dir, 'generate.js'), 'w') as f:
    f.write(api_code)

print('Vercel Backend setup complete.')
