from PIL import Image, ImageDraw, ImageFont

# Open the current logo
current_logo_path = "logo.png"
current_logo = Image.open(current_logo_path)

# Create a new image with the same size as the current logo
new_logo = Image.new("RGBA", current_logo.size, (255, 255, 255, 0))

# Draw the letters "DL" on the new image
draw = ImageDraw.Draw(new_logo)
font_size = int(current_logo.size[1] * 0.8)  # Adjust font size based on logo height
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)
text = "DL"
bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
text_position = ((new_logo.size[0] - text_width) // 2, (new_logo.size[1] - text_height) // 2)

# Fill the background with white
draw.rectangle([(0, 0), new_logo.size], fill="white")

# Draw the text in the center
draw.text(text_position, text, font=font, fill="black")

# Save the new logo
new_logo_path = "logo_new.png"
new_logo.save(new_logo_path)

print(f"New logo saved to {new_logo_path}")