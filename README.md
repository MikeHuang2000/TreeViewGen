# TreeViewGen
 File-Structure-TreeView-Generator



用于生成类似以下结构的文件TreeView文本图

> D:\ISO
>
> │  grldr
>
> │
>
> └─boot
>
>  │  bcd
>
>  │  boot.sdi
>
>  │  bootmgr
>
>  │  wimboot
>
>  │
>
>  ├─grub
>
>  │      menu.lst
>
>  │
>
>  ├─w10pe32
>
>  │      boot.wim
>
>  │
>
>  └─w10pe64
>
> ​         boot.wim
>
> 

输入示例（input.txt）：

> A B
>
> A C
>
> B D
>
> B E
>
> C F
>
> 
>
> //输入格式：父节点+空格+子节点
> //默认第一个输入的父节点是根节点

输出示例（output.txt）：

> A
>
> ├─ B
>
> │   ├─ D
>
> │   │
>
> │   └─ E
>
> └─ C
>
>  └─ F
>
> 

