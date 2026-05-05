#!/usr/bin/env python3
"""
Create 3 header/banner images for Midnight Pro V2 website
Size: 800x450px (16:9)
Style: Abstract dark luxury with gold accents
"""

from PIL import Image, ImageDraw, ImageFilter, ImageFont
import math
import random

# Set random seed for reproducibility
random.seed(42)

def create_gradient_background(width, height, color_stops):
    """Create a vertical gradient background"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        # Find which color stops we're between
        for i in range(len(color_stops) - 1):
            if ratio <= color_stops[i + 1][0]:
                local_ratio = (ratio - color_stops[i][0]) / (color_stops[i + 1][0] - color_stops[i][0])
                r = int(color_stops[i][1][0] + (color_stops[i + 1][1][0] - color_stops[i][1][0]) * local_ratio)
                g = int(color_stops[i][1][1] + (color_stops[i + 1][1][1] - color_stops[i][1][1]) * local_ratio)
                b = int(color_stops[i][1][2] + (color_stops[i + 1][1][2] - color_stops[i][1][2]) * local_ratio)
                draw.line([(0, y), (width, y)], fill=(r, g, b))
                break
    
    return img

def add_geometric_patterns(draw, width, height, color, count=20):
    """Add subtle geometric patterns"""
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(20, 80)
        opacity = random.randint(10, 30)
        pattern_color = (color[0], color[1], color[2], opacity)
        
        shape_type = random.choice(['line', 'circle', 'rect'])
        if shape_type == 'line':
            angle = random.uniform(0, math.pi)
            x2 = x + int(size * math.cos(angle))
            y2 = y + int(size * math.sin(angle))
            draw.line([(x, y), (x2, y2)], fill=color[:3], width=1)
        elif shape_type == 'circle':
            draw.ellipse([x, y, x + size, y + size], outline=color[:3], width=1)
        else:
            draw.rectangle([x, y, x + size, y + size], outline=color[:3], width=1)

def add_light_rays(img, draw, width, height, center_x, center_y, color):
    """Add subtle light rays emanating from a point"""
    num_rays = 12
    for i in range(num_rays):
        angle = (2 * math.pi * i) / num_rays
        end_x = center_x + int(width * 0.8 * math.cos(angle))
        end_y = center_y + int(height * 0.8 * math.sin(angle))
        
        # Draw multiple lines for gradient effect
        for offset in range(-2, 3):
            ox = offset * math.sin(angle)
            oy = offset * math.cos(angle)
            alpha = int(15 - abs(offset) * 5)
            ray_color = (color[0], color[1], color[2])
            draw.line([(center_x + ox, center_y + oy), (end_x + ox, end_y + oy)], 
                     fill=ray_color, width=2)

def add_particles(draw, width, height, color, count=30):
    """Add small particle dots"""
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.choice([1, 1, 2, 2, 3])
        draw.ellipse([x, y, x + size, y + size], fill=color)

def add_sparkles(draw, width, height, color, count=15):
    """Add sparkle/star effects"""
    for _ in range(count):
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        size = random.randint(8, 20)
        
        # Draw cross sparkle
        draw.line([(x - size, y), (x + size, y)], fill=color, width=1)
        draw.line([(x, y - size), (x, y + size)], fill=color, width=1)
        
        # Small center dot
        draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=color)

def add_gold_lines(draw, width, height, color, count=5):
    """Add elegant gold accent lines"""
    for _ in range(count):
        # Horizontal accent lines
        y = random.randint(height // 4, 3 * height // 4)
        x_start = random.randint(0, width // 3)
        x_end = x_start + random.randint(100, 250)
        draw.line([(x_start, y), (x_end, y)], fill=color, width=1)
        
        # Add small dots at ends
        draw.ellipse([x_start - 2, y - 2, x_start + 2, y + 2], fill=color)
        draw.ellipse([x_end - 2, y - 2, x_end + 2, y + 2], fill=color)

def add_connectivity_motifs(draw, width, height, color):
    """Add subtle connectivity/network motifs"""
    # Create a few node points
    nodes = []
    for _ in range(5):
        nodes.append((random.randint(100, width - 100), random.randint(100, height - 100)))
    
    # Draw connections between nearby nodes
    for i, node1 in enumerate(nodes):
        for node2 in nodes[i+1:]:
            dist = math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)
            if dist < 200:
                draw.line([node1, node2], fill=color, width=1)
        
        # Draw node
        draw.ellipse([node1[0] - 3, node1[1] - 3, node1[0] + 3, node1[1] + 3], fill=color)

def get_font(size):
    """Try to get a nice font, fallback to default"""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Helvetica.dfont",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]
    
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    
    return ImageFont.load_default()

def add_text_with_glow(img, draw, text, y_position, width, gold_color, shadow_color):
    """Add elegant text with subtle glow effect"""
    font_large = get_font(42)
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) // 2
    
    # Draw shadow/glow layers
    for offset in range(3, 0, -1):
        alpha_factor = 0.3 + (3 - offset) * 0.15
        shadow = tuple(int(c * alpha_factor) for c in shadow_color[:3])
        draw.text((x, y_position), text, font=font_large, fill=shadow)
    
    # Draw main text
    draw.text((x, y_position), text, font=font_large, fill=gold_color)
    
    # Add underline accent
    line_y = y_position + 55
    line_width = text_width + 40
    line_x = (width - line_width) // 2
    draw.line([(line_x, line_y), (line_x + line_width, line_y)], fill=gold_color, width=2)
    
    # Add decorative dots at ends of line
    draw.ellipse([line_x - 4, line_y - 4, line_x + 4, line_y + 4], fill=gold_color)
    draw.ellipse([line_x + line_width - 4, line_y - 4, line_x + line_width + 4, line_y + 4], fill=gold_color)

def create_why_choose_us_header():
    """Create Why Choose Us header"""
    width, height = 800, 450
    
    # Midnight gradient colors
    color_stops = [
        (0.0, (10, 15, 30)),      # Top: deep midnight
        (0.5, (20, 25, 45)),      # Middle
        (1.0, (5, 10, 25))        # Bottom: darker
    ]
    
    img = create_gradient_background(width, height, color_stops)
    draw = ImageDraw.Draw(img)
    
    # Add geometric patterns
    add_geometric_patterns(draw, width, height, (212, 175, 55), count=25)
    
    # Add light rays from top center
    add_light_rays(img, draw, width, height, width // 2, -50, (212, 175, 55))
    
    # Add gold particles
    add_particles(draw, width, height, (212, 175, 55), count=40)
    
    # Add accent lines
    add_gold_lines(draw, width, height, (212, 175, 55), count=6)
    
    # Add text
    add_text_with_glow(img, draw, "Why Choose Us", 180, width, 
                      (212, 175, 55), (100, 85, 40))
    
    return img

def create_testimonials_header():
    """Create Client Testimonials header"""
    width, height = 800, 450
    
    # Midnight gradient colors
    color_stops = [
        (0.0, (12, 18, 35)),
        (0.5, (22, 28, 50)),
        (1.0, (8, 12, 28))
    ]
    
    img = create_gradient_background(width, height, color_stops)
    draw = ImageDraw.Draw(img)
    
    # Add subtle geometric patterns
    add_geometric_patterns(draw, width, height, (212, 175, 55), count=20)
    
    # Add sparkles/stars
    add_sparkles(draw, width, height, (212, 175, 55), count=20)
    
    # Add particles
    add_particles(draw, width, height, (212, 175, 55), count=35)
    
    # Add accent lines
    add_gold_lines(draw, width, height, (212, 175, 55), count=5)
    
    # Add text
    add_text_with_glow(img, draw, "Client Testimonials", 180, width,
                      (212, 175, 55), (100, 85, 40))
    
    return img

def create_contact_header():
    """Create Get In Touch header"""
    width, height = 800, 450
    
    # Midnight gradient colors
    color_stops = [
        (0.0, (8, 15, 30)),
        (0.5, (18, 25, 48)),
        (1.0, (5, 10, 25))
    ]
    
    img = create_gradient_background(width, height, color_stops)
    draw = ImageDraw.Draw(img)
    
    # Add geometric patterns
    add_geometric_patterns(draw, width, height, (212, 175, 55), count=22)
    
    # Add connectivity motifs
    add_connectivity_motifs(draw, width, height, (180, 150, 80))
    
    # Add particles
    add_particles(draw, width, height, (212, 175, 55), count=30)
    
    # Add accent lines
    add_gold_lines(draw, width, height, (212, 175, 55), count=6)
    
    # Add text
    add_text_with_glow(img, draw, "Get In Touch", 180, width,
                      (212, 175, 55), (100, 85, 40))
    
    return img

def main():
    output_dir = "/Users/billyagent/.openclaw/workspace-picasso/projects/designs/template-midnight-pro-v2/images/"
    
    print("Creating Why Choose Us header...")
    img1 = create_why_choose_us_header()
    img1.save(f"{output_dir}why-choose-us-header.jpg", "JPEG", quality=95)
    print(f"  Saved: why-choose-us-header.jpg")
    
    print("Creating Client Testimonials header...")
    img2 = create_testimonials_header()
    img2.save(f"{output_dir}testimonials-header.jpg", "JPEG", quality=95)
    print(f"  Saved: testimonials-header.jpg")
    
    print("Creating Get In Touch header...")
    img3 = create_contact_header()
    img3.save(f"{output_dir}contact-header.jpg", "JPEG", quality=95)
    print(f"  Saved: contact-header.jpg")
    
    print("\nAll header images created successfully!")

if __name__ == "__main__":
    main()
