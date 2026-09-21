# Chanseok Lee — Academic Homepage

Personal academic website for Chanseok Lee, postdoctoral researcher at KAIST.

**Live site:** https://csleemooo.github.io/

## Structure

- `index.html`: biography, research, publications, experience, honors, and contact
- `styles.css`: responsive visual design
- `script.js`: accessible mobile navigation
- `assets/`: supplied portrait
- `tools/github_publish.py`: deployment helper using the local Git Credential Manager; contains no credentials

This is a static site with no build or installation requirement. GitHub Pages serves the root of the `main` branch. Pushing to `main` updates the site automatically.

## Local preview

Run `python -m http.server 4173 --bind 127.0.0.1` from this directory, then open http://127.0.0.1:4173/.

## Maintaining content

Edit text and publication entries in `index.html`. The portrait is the supplied original; it is displayed without retouching. Update `sitemap.xml` after substantive changes. Original CV and research-summary PDFs are not published; this site contains the curated professional profile only.

Content is based on the owner's CV and research summary, dated September 21, 2026. Publication metadata is checked against publisher records. DeepPhaseCut uses its 2022 journal issue year, and the diffusion preprint follows the latest arXiv author list including Jongin You. Publications in preparation are not represented as published.

## Design and accessibility

The site uses semantic HTML, keyboard focus indicators, a skip link, reduced-motion support, and responsive layouts. Content remains available without JavaScript. Google Fonts provides Manrope and DM Sans, with system fallbacks. No analytics, cookies, contact form, or tracking scripts are included.

## 향후 수정

이 폴더가 홈페이지 원본입니다. 이 Codex 작업에서 변경 내용을 요청하면 소스 수정 후 GitHub에 반영할 수 있습니다. 개인정보가 담긴 새 자료는 공개 범위를 확인해 반영합니다. 인증 토큰이나 비밀번호를 소스에 저장하지 않습니다.
