> **Note**
> 
> **ChatPaper已经完成了近五年5w篇顶会论文总结，可以助你在科研道路更加顺利：https://chatpaper.org/**

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

<center><kbd><img src="./docs/images/usage.png" height="550px"/></kbd></center>

<p align="center">
      <em>一站式服务 / 简单 / 快速 / 高效 / 智能</em>
      <br/>
      <a href="#"><strong>视频教程</strong></a>
      <a href="https://github.com/WangRongsheng/ChatGenTitle/releases/tag/LLaMa-Lora-7B-cs-6-new-app"><strong>安装部署</strong></a>
      <a href="https://drive.google.com/file/d/1akrC4-YnYdiyD1_VK-92hncN7HS0FLf5/view?usp=sharing" target="_parent"><strong>在线体验</strong></a>
    </p>

# News

- 🎉🎉 所有人可以在线免费体验ChatGenTitle，<a href="https://drive.google.com/file/d/1akrC4-YnYdiyD1_VK-92hncN7HS0FLf5/view?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> ；
- 🎉🎉 由于缺乏GPU计算资源，我们发布了[在线部署版本](https://github.com/WangRongsheng/ChatGenTitle/releases/tag/LLaMa-Lora-7B-cs-6-new-app) 的所有代码和权重，可以在任何环境部署使用；
- 🎉🎉 arXiv上每天都会产生大量与LLMs相关的工作，该仓库每日自动推送30篇LLMs相关的论文供大家学习，[点击学习今日LLMs论文](https://github.com/WangRongsheng/ChatGenTitle/blob/main/LLMs-papers.md)
- 🎉🎉 正式发布[LLaMa-Lora-7B-3](https://drive.google.com/file/d/1c1uUizHP7jatrj6GxtppGYgZSKPWSExs/view?usp=sharing) 和 [LLaMa-Lora-7B-3-new](https://drive.google.com/file/d/1AuxbIzMXLX89TUPQTrEF2K-IyhF3OKiZ/view?usp=sharing) 版本的LoRA模型权重，允许本地部署使用；
- 🎉🎉 完成了基于[alpaca-lora](https://github.com/tloen/alpaca-lora) 上进行的`LLaMa-Lora-7B-3`和`LLaMa-Lora-13B-3`模型微调；
- 🎉🎉 开始了一项长期进行在`arXiv`上定时爬取[cs.AI](http://export.arxiv.org/rss/cs.AI) 、[cs.CV](http://export.arxiv.org/rss/cs.CV) 、[cs.LG](http://export.arxiv.org/rss/cs.LG) 论文的任务，目的是为了支持 CS 相关方向的研究；
- 🎉🎉 整理了`220W+`篇arXiv论文的元信息，这些元信息包括：`title`和`abstract`，更多的有：`id`、`submitter`、`authors`、`comments`、`journal-ref`、`doi`、`categories`、`versions`；

## TODO

* [ ] 完成LoRA对大模型微调的教程
* [ ] 发布arXiv（很快完成...）
* [X] 完成ChatGenTitle、ChatGPT、GPT4的效果对比
* [X] 发布在线使用版本，[LLaMa-Lora-7B-cs-6-new-app](https://github.com/WangRongsheng/ChatGenTitle/releases/tag/LLaMa-Lora-7B-cs-6-new-app) <a href="https://drive.google.com/file/d/1akrC4-YnYdiyD1_VK-92hncN7HS0FLf5/view?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Release

> **Note**
> 
> Meta发布的LLaMA模型禁止商用，因此这里我们开源的是LoRA模型，LoRA模型必须搭配对应版本的LLaMA模型使用才可以，具体请看[Chinese-LLaMA-Alpaca
#合并模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca#%E5%90%88%E5%B9%B6%E6%A8%A1%E5%9E%8B)

|模型名称|微调数据|微调基准模型|模型大小|微调时长|微调效果|
|:-|:-|:-|:-|:-|:-|
|✅[LLaMa-Lora-7B-3](https://huggingface.co/wangrongsheng/chatgentitle-lora-all-3)|arXiv-50-all|LLaMa-7B|-MB|9 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/7b-50-3-new.png)|
|✅[LLaMa-Lora-7B-3-new](https://huggingface.co/wangrongsheng/chatgentitle-lora-all-3-new) |arXiv-50-all|LLaMa-7B|-MB|12.5 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/7b-50-3-new.png)|
|✅[LLaMa-Lora-7B-cs-3-new](https://huggingface.co/wangrongsheng/chatgentitle-lora-cs-3-new) |arXiv-cs |LLaMa-7B|-MB|20.5 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/7b-cs-3.png)|
|✅[LLaMa-Lora-7B-cs-6-new](https://huggingface.co/wangrongsheng/chatgentitle-lora-cs-6-new) |arXiv-cs|LLaMa-7B|-MB|34 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/usage.png)|
|♻️LLaMa-Lora-13B-3|arXiv-100-all|LLaMa-13B|-MB|26 hours|[点击查看](https://github.com/WangRongsheng/ChatGenTitle/blob/main/docs/images/13B-100-3.png)|

<details>
  <summary>训练设置</summary>
  <p>* 实验在A100 (4X, 80GB)上进行</p>
</details>

# Comparison

|提示词|摘要|原始论文题目|**ChatGenTitle**|ChatGPT(GPT3.5)|GPT4|
|:-|:-|:-|:-|:-|:-|
|提示词①|摘要①|Focus-RCNet: A lightweight recyclable waste classification algorithm based on Focus and knowledge distillation|Focus-RCNet: A Lightweight Convolutional Neural Network for Recyclable  Waste Image Classification|Focus-RCNet: A lightweight deep learning model for automated waste classification with enhanced recyclable waste image feature recognition|Efficient Waste Classification with Focus-RCNet: A Lightweight Deep Learning Architecture Employing Sandglass Structure, SimAM Attention Mechanism, and Knowledge Distillation for Real-Time Embedded Applications|
|提示词②|摘要②|ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices|ShuffleNet: Efficient Convolutional Neural Networks for Mobile Devices|ShuffleNet: A Computation-Efficient CNN Architecture for Mobile Devices with Superior Performance in Object Detection and ImageNet Classification while Maintaining Accuracy|ShuffleNet: A Computationally Efficient CNN Architecture for Mobile Devices with Enhanced Performance in ImageNet Classification and MS COCO Object Detection|
|提示词③|摘要③|Segment Anything|Segment Anything|Segment Anything: Introducing a New Task, Model, and Dataset for Promptable Image Segmentation with Superior Zero-Shot Performance|Exploring the Segment Anything Project: A Promptable Image Segmentation Model and Extensive Dataset with Impressive Zero-Shot Performance|

<details>
  <summary>1. 提示词①和摘要①</summary>
  
- 提示词①：If you are an expert in writing papers, please generate a good paper title for this paper based on other authors' descriptions of their abstracts.
- 摘要①：Waste pollution is one of the most important environmental problems in the modern world. With the continuous improvement of the living standard of the population and the increasing richness of the consumption structure, the amount of domestic waste generated has increased dramatically and there is an urgent need for further waste treatment of waste. The rapid development of artificial intelligence provides an effective solution for automated waste classification. However, the large computational power and high complexity of algorithms make convolutional neural networks (CNNs) unsuitable for real-time embedded applications. In this paper, we propose a lightweight network architecture, Focus-RCNet, designed with reference to the sandglass structure of MobileNetV2, which uses deeply separable convolution to extract features from images. The Focus module is introduced into the field of recyclable waste image classification to reduce the dimensionality of features while retaining relevant information. In order to make the model focus more on waste image features while keeping the amount of parameters computationally small, we introduce the SimAM attention mechanism. Additionally, knowledge distillation is used to further compress the number of parameters in the model. By training and testing on the TrashNet dataset, the Focus-RCNet model not only achieves an accuracy of 92%, but also has high mobility of deployment.

</details>

<details>
  <summary>2. 提示词②和摘要②</summary>
  
- 提示词②：If you are an expert in writing papers, please generate a good paper title for this paper based on other authors' descriptions of their abstracts.
- 摘要②：We introduce an extremely computation-efficient CNN architecture named ShuffleNet, which is designed specially for mobile devices with very limited computing power (e.g., 10-150 MFLOPs). The new architecture utilizes two new operations, pointwise group convolution and channel shuffle, to greatly reduce computation cost while maintaining accuracy. Experiments on ImageNet classification and MS COCO object detection demonstrate the superior performance of ShuffleNet over other structures, e.g. lower top-1 error (absolute 7.8%) than recent MobileNet on ImageNet classification task, under the computation budget of 40 MFLOPs. On an ARM-based mobile device, ShuffleNet achieves ~13x actual speedup over AlexNet while maintaining comparable accuracy.

</details>

<details>
  <summary>3. 提示词③和摘要③</summary>
  
- 提示词③：If you are an expert in writing papers, please generate a good paper title for this paper based on other authors' descriptions of their abstracts.
- 摘要③：We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images.

</details>

# Reference

> **Note**
> 
> 时代在进步，大模型（LLMs）也是，所以你可以每天来读30篇最新的关于LLM的Paper，保证你的知识不会跟丢！
> 
> 👉👉👉[**查看今日LLMs论文**](https://github.com/WangRongsheng/ChatGenTitle/blob/main/LLMs-papers.md)

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
