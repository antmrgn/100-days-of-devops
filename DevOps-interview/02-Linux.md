**Q: How to check size of file or directory**  
**A:**  

size of file:
```
ls -lh {path to file}  
```
  
size of directory:
```
du -hs  
```
  
size of all directory with sort by size:
```
du -h --max-depth=1 {path to dir} | sort -hr  
```
 