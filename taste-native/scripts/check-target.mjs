import fs from 'node:fs';
const config=JSON.parse(fs.readFileSync(new URL('../audit-target.json',import.meta.url)));
const url=new URL(String(config.public_url||''));
if(url.protocol!=='https:'||url.port||url.username||url.password||!['rgym.bg','gspace.bg','example.com'].includes(url.hostname.toLowerCase())||url.hash){
 throw new Error('Refusing unapproved public target URL');
}
console.log(url.toString());