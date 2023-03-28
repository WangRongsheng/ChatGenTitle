数据存储：

- 按照时间日期保存
- 保存格式：
```html
{
"instruction": "If you are a doctor, please answer the medical questions based on the patient's description.",
"input": "Doctor, I have been experiencing a hoarse voice for a few weeks now and it's not getting any better despite taking medication. What could be the problem?",
"output": "It's possible that you have a vocal cord polyp. To confirm this, we need to conduct tracheoscopy and laryngoscopy with a biopsy. We may also need to conduct an occupational therapy assessment such as speech therapy, other diagnostic procedures like an interview or consultation, physical therapy exercises, as well as diagnostic procedures on your nose, mouth, and pharynx to rule out any other underlying conditions. Additionally, we may need to evaluate your eyes and ears for any related conditions, such as ophthalmologic and otologic diagnosis and treatment."
}

- instruction：system role
- input：论文摘要
- output: 论文题目
```

- 爬取目标：[https://arxiv.org/](https://arxiv.org/)