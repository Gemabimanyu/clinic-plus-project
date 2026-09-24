// Membuat PDF format layar HP dari 00-BUKU-LENGKAP.md.
// Pakai: npm install marked playwright   lalu   node docs/buku/tools/render-pdf.js
// Hasil: docs/buku/export/ADVANCED-ENGINE-TUNING-mobile.pdf
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const mdPath = path.join(root, '00-BUKU-LENGKAP.md');
const outPdf = path.join(root, 'export', 'ADVANCED-ENGINE-TUNING-mobile.pdf');
const outHtml = path.join(root, 'export', 'book.html');

marked.setOptions({ gfm: true, breaks: false });
const bodyHtml = marked.parse(fs.readFileSync(mdPath, 'utf-8'));

const html = `<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Advanced Engine Tuning</title>
<style>
  @page { size: 390px 844px; margin: 14px 16px; }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
         font-size: 12.5px; line-height: 1.5; color: #1a1a1a; overflow-wrap: break-word; }
  h1 { font-size: 19px; line-height: 1.25; margin: 0 0 8px; padding: 6px 0; border-bottom: 2px solid #1a1a1a; page-break-before: always; }
  body > h1:first-of-type { page-break-before: avoid; }
  h2 { font-size: 15.5px; line-height: 1.3; margin: 16px 0 6px; padding: 2px 0 3px; border-bottom: 1px solid #ccc; page-break-after: avoid; }
  h3 { font-size: 13.5px; margin: 12px 0 5px; page-break-after: avoid; }
  p { margin: 6px 0; orphans: 2; widows: 2; }
  ul, ol { margin: 6px 0; padding-left: 18px; }
  li { margin: 2px 0; }
  hr { border: none; border-top: 1px solid #ccc; margin: 14px 0; }
  blockquote { margin: 8px 0; padding: 6px 10px; border-left: 3px solid #444; background: #f4f4f4; font-style: italic; }
  code { font-family: "SFMono-Regular", Menlo, Consolas, monospace; font-size: 10.5px; background: #f0f0f0; padding: 1px 3px; border-radius: 3px; word-break: break-word; }
  pre { background: #f4f4f4; padding: 8px; border-radius: 4px; white-space: pre-wrap; font-size: 10.5px; line-height: 1.4; margin: 8px 0; }
  pre code { background: none; padding: 0; }
  table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 10.5px; table-layout: fixed; }
  th, td { border: 1px solid #ccc; padding: 3px 4px; text-align: left; vertical-align: top; overflow-wrap: break-word; }
  th { background: #eaeaea; }
  tr { page-break-inside: avoid; }
</style>
</head>
<body>
${bodyHtml}
</body>
</html>`;

fs.writeFileSync(outHtml, html, 'utf-8');

(async () => {
  // Di lingkungan dengan Chromium terpasang di lokasi lain, isi PW_CHROMIUM dengan path-nya.
  const browser = await chromium.launch(process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {});
  const page = await browser.newPage();
  await page.goto('file://' + outHtml, { waitUntil: 'load' });
  await page.pdf({ path: outPdf, width: '390px', height: '844px', printBackground: true,
                   margin: { top: '0px', bottom: '0px', left: '0px', right: '0px' } });
  await browser.close();
  fs.unlinkSync(outHtml);
  console.log('PDF ditulis ke', outPdf);
})();
