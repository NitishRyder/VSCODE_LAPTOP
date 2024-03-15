"""import hashlib

h=hashlib.new("md5")
correct_password="MyPassword123567"
h.update(correct_password.encode())

password_hash=h.hexdigest()
print(password_hash)

user_input="MyPassword123567"
h=hashlib.new("md5")
h.update(user_input.encode())
input_hash=h.hexdigest()

print(input_hash==password_hash)"""

import cv2
import hashlib

def compute_md5_hash(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise Exception("Image not found or could not be read.")
        
        md5_hash = hashlib.md5()
        with open(image_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        
        return md5_hash.hexdigest()
    
    except Exception as e:
        print("Error:", e)
        return None

def main():
    image_path1 = "D:\Pictures\images.jpg"
    image_path2 =  "D:\Pictures\images.jpg"#"D:\Pictures\Colorful-4k-Birds-HD-wallpapers-for-pc.jpg"
    
    md5_hash1 = compute_md5_hash(image_path1)
    md5_hash2 = compute_md5_hash(image_path2)
    
    if md5_hash1 and md5_hash2:
        print("MD5 Hash for Image 1:", md5_hash1)
        print("MD5 Hash for Image 2:", md5_hash2)
        
        if md5_hash1 == md5_hash2:
            print("The images have the same MD5 hash. They are identical.")
        else:
            print("The images have different MD5 hashes. They are likely different.")
    else:
        print("MD5 hash computation failed for one or both images.")

if __name__ == "__main__":
    main()