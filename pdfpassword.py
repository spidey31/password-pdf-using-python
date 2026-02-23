import os
from pypdf import PdfReader, PdfWriter


def protect_pdf(input_path, user_password):

    # Check if the file actually exists before doing anything
    if not os.path.exists(input_path):
        print(f"\nOops! Could not find the file: '{input_path}'")
        print("Make sure the file name and path are correct.")
        return

    # Auto-create output name like: myfile_protected.pdf
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_protected{ext}"

    # Read the original PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Copy every page into the new writer
    for page in reader.pages:
        writer.add_page(page)

    # Lock the PDF with the password
    writer.encrypt(user_password=user_password, owner_password=user_password)

    # Save the new protected PDF
    with open(output_path, "wb") as protected_file:
        writer.write(protected_file)

    print("\n✅ Your PDF is now password protected!")
    print(f"   Saved as    : {output_path}")
    print(f"   Total pages : {len(reader.pages)}")
    print(f"   Password    : {user_password}")


# ─── Interactive Input ────────────────────────────────────────────────────────

print("=" * 45)
print("       PDF Password Protector")
print("=" * 45)

input_pdf = input("\nEnter the path of your PDF file : ")
password  = input("Enter the password to protect it : ")

protect_pdf(input_pdf.strip(), password.strip())