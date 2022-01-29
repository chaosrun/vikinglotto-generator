# vikinglotto-generator

本程序用于生成一组 [Vikinglotto](https://en.wikipedia.org/wiki/Vikinglotto) 的机选彩票号码，
输出的结果支持通过 `cowsay` 来显示，以增加趣味性。生成过的号码会记录在日志文件中，以便有需要时查验。

[English instruction](./README.md)

## 依赖

如果需要程序以 `cowsay` 的形式来显示结果，则需要系统中安装 `cowsay`。

以 Debian & Ubuntu 为例：

```bash
sudo apt update
sudo apt install cowsay -y
```

## 安装

使用 pip：

```bash
python3 -m pip install vikinglotto
```

## 用法

以 `cowsay` 模式运行程序：

```bash
vikinglotto
```

不使用 `cowsay`，直接打印结果：

```bash
vikinglotto --plain
```
