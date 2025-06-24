# 🧬 Evolutionary Algorithm

**Project Title:** Evolutionary Algorithm for Template Matching using Natural Selection Principles

---

## 👨‍🔬 Project Overview

This project implements image template matching using evolutionary algorithms inspired by **Darwin's Theory of Natural Selection**. Instead of traditional pattern matching, the algorithm simulates evolution via **selection**, **crossover**, and **mutation** to find image segments that match a given template.

---

## 🧠 Team Members

* 👨‍💻 **Group Leader:** Zia Ur Rehman
* 🧑‍💻 **Members:** Noor Nabi, Shahrukh Khan

---

## 📖 Table of Contents

* [📖 Abstract](#-abstract)
* [🌱 Natural Phenomenon](#-natural-phenomenon)
* [📚 Charles Darwin's Theory](#-charles-darwins-theory)
* [🔬 Evolution](#-evolution)
* [🧪 Model](#-model)
* [💻 Application](#-application)

  * [🖼 Import Image](#-import-image)
  * [✂️ Slicing](#-slicing)
  * [⚙️ Initialization](#-initialization)
  * [🔢 Sorting](#-sorting)
  * [🧬 Crossover and Mutation](#-crossover-and-mutation)
  * [🛑 Termination](#-termination)
* [🧪 Testing](#-testings)
* [✅ Conclusion](#-conclusion)
* [🔗 References](#-references)

---

## 📖 Abstract

Instead of traditional programming techniques, this algorithm replicates **Darwinian evolution** by initializing a population and improving each generation based on fitness. The ultimate goal is to find a match between a template image and the best-fitting region in a larger image.

---

## 🌱 Natural Phenomenon

Darwin's theory revolves around survival of the fittest. Organisms evolve and adapt by selecting traits that maximize survival. This concept is used in this algorithm by generating, evaluating, and evolving image segments.

![Evolution](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/008.png)

---

## 📚 Charles Darwin's Theory

* Species evolve through small, beneficial adaptations.
* Favorable traits are preserved, unfavorable ones are eliminated.
* Populations diverge over time into new species (macroevolution).

---

## 🔬 Evolution

* Overpopulation and competition drive evolution.
* Offspring with superior traits survive.
* **Speciation** can be allopatric (geographic) or sympatric (genetic drift).

---

## 🧪 Model

* Population of image slices is initialized.
* Fitness is measured using **correlation** with the target template.
* Top individuals survive and generate the next generation using **crossover** and **mutation**.

![Model](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/009.jpeg)

---

## 💻 Application

### 🖼 Import Image

Images are converted into 2D grayscale matrices using Python (matplotlib).

### ✂️ Slicing

The large image is randomly sliced into smaller segments (same size as template) based on random coordinates.

### ⚙️ Initialization

Initial random population of image segments is generated. Fitness is calculated via **Pearson correlation**. NumPy is used for optimization.

### 🔢 Sorting

Fitness values are sorted in descending order to select top candidates.

### 🧬 Crossover and Mutation

* Genetic operators applied to top individuals.
* Mutation done on significant bits or coordinates.
* Optimal parameters: 95% crossover, 0.5% mutation.

### 🛑 Termination

Process continues until a desired correlation threshold (e.g. 0.9) is reached.

---

## 🧪 Testing

* With larger populations (e.g. 1000), convergence to high correlation is faster.
* Randomization affects consistency of improvement.
* Best results require tuning mutation/crossover logic.

![Results](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/010.png)
![Results](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/011.jpeg)
![Results](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/012.png)
![Fix](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/013.jpeg)

---

## ✅ Conclusion

The algorithm demonstrates how biological logic can be adapted into computational models. While not always producing a steadily increasing fitness graph, evolutionary methods offer flexibility and resilience. Increasing initial population size significantly improves results.

---

## 🔗 References

1. [Live Science](https://www.livescience.com/474-controversy-evolution-works.html)
2. [Khan Academy on Speciation](https://www.khanacademy.org/science/ap-biology/natural-selection/speciation)
