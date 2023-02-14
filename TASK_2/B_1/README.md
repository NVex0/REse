E sửa tại các chỗ sau:
  * Phần Signature : `CF 50 22 26 0D 6D 61 72`  =>  `89 50 4E 47 0D 0A 1A 0A`
  
  * Chunk IHDR : `49 78 44 20` => `49 48 44 52`
  
  * Chunk IDAT đầu tiên : `49 44 41 0B` => `49 44 41 54`
  
  ![image](https://user-images.githubusercontent.com/113530029/218783947-327d75b7-ef40-4587-856f-a7875ed7b7a2.png)

  * EOF : `49 45 7A 2A AE 42 04 82` => `49 45 4E 44 AE 42 60 82`
  
  ![image](https://user-images.githubusercontent.com/113530029/218784183-b26b1127-cbe2-4f6a-bfa6-3ce3ca55e1cf.png)
