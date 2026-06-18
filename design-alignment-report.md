# Design Alignment Report

_Generated: 2026-06-18_
_Figma: [Codebase-Figma-Demo](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/Codebase-Figma-Demo)_

## 1. Implemented vs. missing components

- [x] `Header` exists in both.
- [x] `Card` exists in both.
- [x] `Button` (primary + secondary variants) exists in both.
- [x] `Footer` exists in both.
- [ ] `RoundButton` exists in code ([src/components/round-button/](src/components/round-button/)) but is missing in Figma.

<details>
<summary>Details</summary>

Matched components by name, case-insensitively.

| Component | Figma node | Code |
|---|---|---|
| header | [16:71](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-71) | [src/components/header/Header.tsx](src/components/header/Header.tsx) |
| card | [16:62](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-62) | [src/components/card/Card.tsx](src/components/card/Card.tsx) |
| button (set) | [16:61](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-61) | [src/components/button/Button.tsx](src/components/button/Button.tsx) |
| footer | [16:77](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-77) | [src/components/footer/Footer.tsx](src/components/footer/Footer.tsx) |

`RoundButton` ([src/components/round-button/RoundButton.tsx](src/components/round-button/RoundButton.tsx)) has no matching Figma component in the `Codebase-Figma-Demo` file. Either add it to Figma or remove it from the codebase if it's unused.

</details>

## 2. Matching component design

- [x] `Header` matches.
- [x] `Card` matches.
- [x] `Button` matches.
- [x] `Footer` matches.
- [ ] `RoundButton` has no Figma equivalent to compare against, and uses hardcoded `40px` instead of the `--size-button-height` token. See [src/components/round-button/RoundButton.module.css](src/components/round-button/RoundButton.module.css).

<details>
<summary>Details</summary>

**`Header`** — [code](src/components/header/Header.module.css) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-71)
- Colors: bg `--color-white` (#FFFFFF) ✓; text `--color-navy` (#1B2A4E) ✓.
- Spacing: padding `0 --space-2xl` (0 64px) ✓; nav gap `--space-lg` (24px) ✓.
- Radius: n/a.
- Typography: logo Inter Bold 16px ✓ (`--font-size-title` + `--font-weight-bold`); nav Inter Regular 14px ✓ (`--font-size-nav`).
- Sizes: height `--size-header-height` (72px) ✓.
- Verdict: match.

**`Card`** — [code](src/components/card/Card.module.css) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-62)
- Colors: card bg `--color-white` ✓; title and description `--color-navy` ✓.
- Spacing: content padding `--space-lg` (24px) ✓; content gap `--space-md` (16px) ✓; text gap `--space-xs` (4px) ✓.
- Radius: `--radius-lg` (12px) ✓.
- Typography: title Inter Bold 16px ✓; description Inter Regular 12px ✓ (`--font-size-subtitle`).
- Sizes: width `--size-card-width` (320px) ✓; image height `--size-card-image-height` (160px) ✓.
- Verdict: match.

**`Button`** — [code](src/components/button/Button.module.css) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-61)
- Colors: primary bg `--color-navy` / text `--color-white` ✓; secondary bg `--color-white` / text `--color-navy` / 1px navy border ✓.
- Spacing: padding `--space-sm --space-md` (8px 16px) ✓; gap `--space-sm` (8px) ✓.
- Radius: `--radius-md` (8px) ✓.
- Typography: Inter Semi Bold 14px ✓ (`--font-size-body` + `--font-weight-semibold`).
- Sizes: border `--size-border` (1px) ✓.
- Verdict: match.

**`Footer`** — [code](src/components/footer/Footer.module.css) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-77)
- Colors: bg `--color-navy` ✓; text `--color-white` ✓.
- Spacing: padding `0 --space-2xl` (0 64px) ✓.
- Radius: n/a.
- Typography: Inter Regular 14px ✓ (`--font-size-body`).
- Sizes: height `--size-footer-height` (80px) ✓.
- Verdict: match (text wording ignored per rules).

**`RoundButton`** — [code](src/components/round-button/RoundButton.module.css) · figma: none
- Cannot compare without a Figma source.
- Code uses hardcoded `width: 40px; height: 40px;` even though `--size-button-height: 40px` exists as a token — refactor candidate, but not a Figma mismatch.

</details>

## 3. Matching layout

- [x] App shell (header, main, footer) order and structure match.
- [x] Header and footer dimensions, paddings, and alignment match.
- [x] Card grid gaps (row 40px, column 64px) and card width (320px) match.
- [ ] Card grid fill order differs: Figma is **column-major** (two vertical columns of 3), code is **row-major** (CSS Grid fills row by row). See [src/pages/home/index.module.css](src/pages/home/index.module.css).
- [ ] Card #3 renders the **secondary** button in code; in Figma all 6 cards use the **primary** button. See [src/pages/home/index.tsx](src/pages/home/index.tsx).

<details>
<summary>Details</summary>

**App shell** — [code](src/App.tsx) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-79)
- Structure: header → main → footer, column. Match.
- Page background: `--color-page-bg` (#E5E7EB) ✓.
- Main padding: `--space-2xl --space-xl` (64px 40px) ✓, centered ✓.

**Card grid** — [code](src/pages/home/index.module.css) · [figma](https://www.figma.com/design/i3MTtBKiPbLq7bEIJqL4yc/?node-id=16-87)
- Gaps: row 40px, column 64px — match.
- Card count: 6 in both — match.
- Fill order — mismatch:
  - Figma: two `column` frames, cards filled top-to-bottom in each column. Visual order on screen: `[1][4] / [2][5] / [3][6]`.
  - Code: `grid-template-columns: repeat(2, var(--size-card-width))`, cards filled left-to-right per row. Visual order: `[1][2] / [3][4] / [5][6]`.
  - Same total 2×3 layout but cards 2–5 land in different positions.
  - Fix options in code: switch to `grid-auto-flow: column` with `grid-template-rows: repeat(3, auto)`, or restructure into two flex columns to match Figma's structure.

**Button variant per card** — [code](src/pages/home/index.tsx)
- Figma: every card instance (#16:89, #16:98, #16:107, #16:117, #16:126, #16:135) references button `componentId: 16:57` (variant=primary).
- Code: `variant={i === 2 ? 'secondary' : 'primary'}` renders the third card with the secondary button.
- Either remove the special case in code or update Figma to show a secondary variant on card #3.

</details>
