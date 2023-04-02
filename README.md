<div align="center">
  <a href="https://github.com/WangRongsheng/ChatGenTitle">
    <img src="https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/logo.png" alt="Logo" height="180">
  </a>

  <p align="center">
    <h3> ChatGenTitle：使用百万arXiv论文信息在LLaMA模型上进行微调的论文题目生成模型 </h3>
    <p align="center">
      <a href="https://github.com/WangRongsheng/ChatGenTitle/blob/main/LICENSE">
        <img alt="GitHub Contributors" src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" />
      </a>
      <a href="https://github.com/WangRongsheng/ChatGenTitle/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/WangRongsheng/ChatGenTitle" />
      </a>
      <a href="https://github.com/WangRongsheng/ChatGenTitle/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/WangRongsheng/ChatGenTitle?color=0088ff" />
      </a>
      <a href="https://github.com/WangRongsheng/ChatGenTitle/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/WangRongsheng/ChatGenTitle?color=0088ff" />
      </a>
      <a href=href="https://github.com/kaixindelele/ChatPaper/stargazers">
        <img src="https://img.shields.io/github/stars/WangRongsheng/ChatGenTitle?color=ccf">
      </a>
  </p>
</div>

# News

- 🎉🎉 正式发布[LLaMa-Lora-7B-3](https://drive.google.com/file/d/1c1uUizHP7jatrj6GxtppGYgZSKPWSExs/view?usp=sharing) 版本的LoRA模型权重，允许本地部署使用；
- 🎉🎉 完成了基于[alpaca-lora](https://github.com/tloen/alpaca-lora) 上进行的`LLaMa-Lora-7B-3`和`LLaMa-Lora-13B-3`模型微调；
- 🎉🎉 开始了一项长期进行在`arXiv`上定时爬取[cs.AI](http://export.arxiv.org/rss/cs.AI) 、[cs.CV](http://export.arxiv.org/rss/cs.CV) 、[cs.LG](http://export.arxiv.org/rss/cs.LG) 论文的任务，目的是为了支持 CS 相关方向的研究；
- 🎉🎉 整理了`220W+`篇arXiv论文的元信息，这些元信息包括：`title`和`abstract`，更多的有：`id`、`submitter`、`authors`、`comments`、`journal-ref`、`doi`、`categories`、`versions`；

# Release

> **Note**
> 
> Meta发布的LLaMA模型禁止商用，因此这里我们开源的是LoRA模型，LoRA模型必须搭配对应版本的LLaMA模型使用才可以，具体请看[Chinese-LLaMA-Alpaca
#合并模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca#%E5%90%88%E5%B9%B6%E6%A8%A1%E5%9E%8B)

|模型名称|微调数据|微调基准模型|模型大小|微调时长|微调效果|
|:-|:-|:-|:-|:-|:-|
|✅[LLaMa-Lora-7B-3](https://drive.google.com/file/d/1c1uUizHP7jatrj6GxtppGYgZSKPWSExs/view?usp=sharing)|arXiv-50-all|LLaMa-7B|148.1MB|9 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/7b-50-3-new.png)|
|✅[LLaMa-Lora-7B-3-new](https://drive.google.com/file/d/1AuxbIzMXLX89TUPQTrEF2K-IyhF3OKiZ/view?usp=sharing) |arXiv-50-all|LLaMa-7B|586MB|12.5 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/7b-50-3-new.png)|
|♻️LLaMa-Lora-13B-3|arXiv-100-all|LLaMa-13B|230.05MB|26 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/13B-100-3.png)|

<details>
  <summary>训练设置</summary>
  <p>* 实验在A100 (4X, 80GB)上进行</p>
</details>

# Reference

- [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca)
- [alpaca-lora](https://github.com/tloen/alpaca-lora)
- [ChatDoctor](https://github.com/Kent0n-Li/ChatDoctor)
- [Chinese-alpaca-lora](https://github.com/LC1332/Chinese-alpaca-lora)
- [cabrita](https://github.com/22-hours/cabrita)
- [japanese-alpaca-lora](https://github.com/masa3141/japanese-alpaca-lora)
- [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)
- [FastChat](https://github.com/lm-sys/FastChat)
- [LLaMA-Adapter](https://github.com/ZrrSkywalker/LLaMA-Adapter)
- [LMFlow](https://github.com/OptimalScale/LMFlow)

# Knowledge

<details>
  <summary>1. 关于Instruct微调和LoRa微调</summary>
  
> Instruct微调和LoRa微调是两种不同的技术。
> Instruct微调是指在深度神经网络训练过程中调整模型参数的过程，以优化模型的性能。在微调过程中，使用一个预先训练好的模型作为基础模型，然后在新的数据集上对该模型进行微调。**Instruct微调是一种通过更新预训练模型的所有参数来完成的微调方法，通过微调使其适用于多个下游应用。**
> LoRa微调则是指对低功耗广域网（LoRaWAN）中的LoRa节点参数进行微调的过程，以提高节点的传输效率。**在LoRa微调中，需要了解节点的硬件和网络部署情况，并通过对节点参数进行微小调整来优化传输效率。与Instruct微调相比，LoRA在每个Transformer块中注入可训练层，因为不需要为大多数模型权重计算梯度，大大减少了需要训练参数的数量并且降低了GPU内存的要求。**
> **研究发现，使用LoRA进行的微调质量与全模型微调相当，速度更快并且需要更少的计算。因此，如果有低延迟和低内存需求的情况，建议使用LoRA微调。**

</details>

<details>
  <summary>2. 为什么会有LLaMA模型和LoRA两种模型？</summary>
  
> 如1所述，模型的微调方式有很多种，基于LoRA的微调产生保存了新的权重，我们可以将生成的LoRA权重认为是一个原来LLaMA模型的[补丁权重](https://github.com/ymcui/Chinese-LLaMA-Alpaca#%EF%B8%8F-%E7%94%A8%E6%88%B7%E9%A1%BB%E7%9F%A5%E5%BF%85%E8%AF%BB) 。至于[LLaMA](https://github.com/facebookresearch/llama) 权重，它则是由Mean公司开源的大模型预训练权重。

</details>


<details>
  <summary>3. 关于词表扩充</summary>
  
> 加入词表是有一定破坏性的， 一是破坏原有分词体系，二是增加了未训练的权重。所以如果不能进行充分训练的话，可能会有比较大的问题。个人觉得如果不是特别专的领域（比如生物医学等涉及很多专业词汇的领域）没有太大必要去扩充英文词表。 [Chinese-LLaMA-Alpaca/issues/16](https://github.com/ymcui/Chinese-LLaMA-Alpaca/issues/16)

</details>



# LICENSE

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

**使用和许可声明**：ChatGenTitle 仅可以在获得许可下供研究使用。

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

# Stargazers
	
[![Stargazers over time](https://starchart.cc/WangRongsheng/ChatGenTitle.svg)](https://starchart.cc/WangRongsheng/ChatGenTitle)

<br><a href="https://github.com/Charmve/computer-vision-in-action#-以用促学先会后懂-"><img align="right" alt="Go for it!" src="https://raw.githubusercontent.com/Charmve/computer-vision-in-action/dd292873828228a753a9bd2de4576dbf8cc3902c/res/ui/footer-rocket.svg" height="220" title="Do what you like, and do it best!"/></a>
<br>
<p align="center">Feel free to ask any questions, open a PR if you feel something can be done differently!</p>
<h2 align="center">🌟 Star this repository 🌟</h2>
<p align="center">Created by <a href="https://github.com/WangRongsheng">WangRongsheng</a></p>
