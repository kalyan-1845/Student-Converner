import { kv } from '@vercel/kv';

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
