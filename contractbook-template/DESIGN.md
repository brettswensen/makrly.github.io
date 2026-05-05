# Contractbook — Style Reference
> Playful professionalism, high-contrast clarity.

**Theme:** Light

Contractbook uses a playful, confident aesthetic with bold primary colors punctuating a clean, spacious light background. The system prioritizes readability and clear interaction points, leveraging vibrant yellow for primary actions and strong blue for statements. Typography is robust and direct, complementing the slightly soft, geometric shapes used throughout components and illustrations. Visual hierarchy is established through strategic color blocking and generous whitespace, rather than relying on complex elevation.

## Tokens — Colors

| Name | Value | Token | Role |
|------|-------|-------|------|
| Washed Black | #1a1a1a | --color-washed-black | Primary text, icon default, borders, dark overlay backgrounds |
| Pure White | #ffffff | --color-pure-white | Page backgrounds, card surfaces, button backgrounds |
| Pearl | #f7f7f3 | --color-pearl | Subtle background for secondary cards and sections |
| Beige | #f0f0ec | --color-beige | Input fields, secondary card backgrounds, muted link backgrounds |
| Ink Black | #000000 | --color-ink-black | Strongest text contrast, button text on light backgrounds |
| Concrete | #d4d4d0 | --color-concrete | Muted text, subtle dividers, inactive states |
| Dim Grey | #6d6868 | --color-dim-grey | Placeholder text, secondary link text |
| Silver Mist | #b3b3b3 | --color-silver-mist | Input field borders, disabled element borders |
| Royal Blue | #1009f6 | --color-royal-blue | Powerful accent color for key cards, button borders, statement headlines |
| Energy Gold | #ffba09 | --color-energy-gold | Primary call-to-action buttons, prominent interactive elements |
| Sky Blue | #add3e5 | --color-sky-blue | Light background for informational cards, decorative accents |
| Deep Moss | #304801 | --color-deep-moss | Rich background for specific content cards or accents |
| Thistle Bloom | #e3c7de | --color-thistle-bloom | Soft accent for illustrations, decorative elements |

## Tokens — Typography

### Abcwhyte
- Substitute: Inter
- Weights: 400, 700
- Sizes: 11px, 12px, 14px, 16px, 25px, 28px, 32px, 40px, 48px

### Type Scale

| Role | Size | Line Height | Token |
|------|------|-------------|-------|
| caption | 11px | 1.4 | --text-caption |
| body | 14px | 1.4 | --text-body |
| heading-sm | 25px | 1.25 | --text-heading-sm |
| heading | 28px | 1.2 | --text-heading |
| heading-lg | 32px | 1.2 | --text-heading-lg |
| display | 48px | 1.2 | --text-display |

## Tokens — Spacing & Shapes

Density: comfortable

### Spacing Scale

| Name | Value | Token |
|------|-------|-------|
| 5 | 5px | --spacing-5 |
| 6 | 6px | --spacing-6 |
| 7 | 7px | --spacing-7 |
| 9 | 9px | --spacing-9 |
| 11 | 11px | --spacing-11 |
| 12 | 12px | --spacing-12 |
| 14 | 14px | --spacing-14 |
| 16 | 16px | --spacing-16 |
| 18 | 18px | --spacing-18 |
| 21 | 21px | --spacing-21 |
| 22 | 22px | --spacing-22 |
| 24 | 24px | --spacing-24 |
| 28 | 28px | --spacing-28 |
| 48 | 48px | --spacing-48 |
| 56 | 56px | --spacing-56 |
| 60 | 60px | --spacing-60 |

### Border Radius

| Element | Value |
|---------|-------|
| tags | 9999px |
| cards | 24px |
| images | 40px |
| inputs | 4.375px |
| buttons | 999px |

### Layout

- Section gap: 60px
- Card padding: 14px
- Element gap: 14px

## Components

### Primary Action Button
Role: Call to action
Filled button with Energy Gold (#ffba09) background and Ink Black (#000000) text, 999px border-radius, 16px vertical / 28px horizontal padding.

### Secondary Ghost Button
Role: Secondary action
Outlined button with transparent background, Washed Black (#1a1a1a) text, 1px border, 999px border-radius, 16px vertical / 14px horizontal padding.

### Accent Card - Royal Blue
Role: Content container
Solid Royal Blue (#1009f6) background, 24px border-radius, 48px internal padding.

### Accent Card - Energy Gold
Role: Content container
Solid Energy Gold (#ffba09) background, 24px border-radius, 48px internal padding.

### Base Card (Rounded)
Role: Content container
Solid Pure White (#ffffff) background, 40px border-radius, 59.5px internal padding.

### Simple Input Field
Role: Data entry
Solid Beige (#f0f0ec) background, Silver Mist (#b3b3b3) 1px border, 4.375px border-radius, 9px vertical / 14px horizontal padding.

## Do's and Don'ts

### Do
- Prioritize Energy Gold (#ffba09) for all primary calls to action
- Use Abcwhyte/Inter font for all text content
- Apply 999px border-radius to all buttons and form fields
- Employ Washed Black (#1a1a1a) for primary text on light backgrounds
- Maintain generous section gaps of 60px
- Utilize Pure White (#ffffff) and Pearl (#f7f7f3) as primary backgrounds

### Don't
- Avoid using multiple font families
- Do not introduce strong drop shadows
- Refrain from complex gradients or textures
- Do not use highly saturated colors for large text areas
- Avoid arbitrary border-radii
- Do not overcrowd sections

## Quick Color Reference
- text: #1a1a1a
- background: #ffffff
- border: #b3b3b3
- accent: #1009f6
- primary action: #ffba09
