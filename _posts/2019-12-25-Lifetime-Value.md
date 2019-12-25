---
layout: post
title: Predicting Lifetime Value
subtitle: With the zero-inflated lognormal (ZILN) distribution
gh-repo: miaojingang/miaojingang.github.io
gh-badge: [star, fork, follow]
tags: [lifetime value, long tail, deep neural networks, Gini coefficient, decile chart]
comments: true
---

Predicting values that are

* long-tailed (with a small number of extremely large values) and/or
* zero-inflated (with a large number of zero values)

can be hard. Examples include

* risk modeling in banking
* loss modeling in insurance.

We have looked into another case: lifetime value -- how much more a customer will spend
after their initial purchase. The zero-inflated lognormal (ZILN) distribution gives
good results.

Please check out
* [github with reproducible colabs](https://github.com/google/lifetime_value)
* Wang, Xiaojing, Liu, Tianqi, and Miao, Jingang. (2019).
  A Deep Probabilistic Model for Customer Lifetime Value Prediction.
  [*arXiv:1912.07753*](https://arxiv.org/abs/1912.07753).


