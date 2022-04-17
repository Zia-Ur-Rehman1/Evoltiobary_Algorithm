# Evoltiobary_Algorithm
11/7/2020  EVOLUTIONARY ![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/001.png)![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/002.png)

ALGORITHM 

Artificial Intelligence

**Group leader: Zia Ur Rehman**

**MEMBERS: NOOR NABI AND  SHAHRUKH KHAN**

## **Abstract** 

In this application, we are trying to implement template-matching technique with a scientific viewpoint. Instead of a programming approach, we are using the phenomena of natural selection and designing an algorithm according to it. Scientific approach of Darwin is implemented by initializing a population and improving each new generation we move towards the best fit. 

Contents 

[........................................................................................................................................................ 1 ](#_page1_x69.00_y72.00)[Introduction .................................................................................................................................................. 1 ](#_page1_x69.00_y597.00)[Natural Phenomenon .................................................................................................................................... 2 ](#_page2_x69.00_y153.00)[**Charles Darwin’s Theory** ........................................................................................................................... 3 ](#_page3_x69.00_y230.00)[Evolution ....................................................................................................................................................... 3 ](#_page3_x69.00_y539.00)[**Model** ............................................................................................................................................................ 4 ](#_page4_x69.00_y424.00)[Application .................................................................................................................................................... 5 ](#_page5_x69.00_y361.00)[Import Image ............................................................................................................................................ 5 ](#_page5_x69.00_y455.00)[Slicing ........................................................................................................................................................ 5 ](#_page5_x69.00_y542.00)[Initialization
............................................................................................................................................... 6 ](#_page6_x69.00_y72.00)[Sorting ....................................................................................................................................................... 6 ](#_page6_x69.00_y288.00)[Crossover and Mutation ........................................................................................................................... 6 ](#_page6_x69.00_y375.00)[Termination ............................................................................................................................................... 6 ](#_page6_x69.00_y560.00)[Conclusion ..................................................................................................................................................... 9 ](#_page9_x69.00_y72.00)[References .................................................................................................................................................... 9 ](#_page9_x69.00_y302.00)

## Introduction 

This report is mainly consist of a method to find a part of image in another image by using the evolutionary method derived from Darwin’s Theory. We have to implement some logical scientific thinking approach to detect the resemblance between two images. In order to do that we have to focus on the evolutionary method of Darwin and design and algorithm based on it. There are many factors involve in evolution and some of them on which we have designed our algorithm are discussed 

## Natural Phenomenon 

Darwin theory is based on natural phenomena. There are two key points in it. First is “everything in the world has some resemblance with each

other” and second one is everything is being modified with the time, generation and environment. Everything is trying his best to survive, evolve and reproduce and this leads them to evolution. 

The nature accepts only those individuals, which are best according to the given environment, and the modification is leading to the survival of best specie to come into existence according to the environment and this is the reason that many other species come to extinct. Natural selection can change species; can divide into further modified and evaluated species and gradually causing a population to change color or size over the course of several generations this is very slow and continuous process, which each new generation the modification is minimum that even sometime we cannot judge. This is called "**microevolution**. “Given enough time and enough accumulated changes, natural selection can create entirely new species, known as "macroevolution." For example, It can turn dinosaurs into birds, amphibious mammals into whales and the ancestors of apes into humans. Wolf are considered the ancestors of dogs and it goes for many more species. 

Darwin also described a form of natural selection that depends on an organism's success at attracting a mate, a process known as sexual selection. The colorful plumage of peacocks and the antlers of male deer are both examples of traits that evolved under this type of selection. [1] 

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/008.png)

## **Charles Darwin’s Theory** 

Actually theory of Darwin was major and pointing step towards relation and resemblance of species of some specific environment. We know, creation on earth is of different kind but may be these kinds are different physically but their initial growth is same. This theory have played vital rule to understand this phenomena of natural selection and then further guided towards evaluated species and organisms, regarding their environment for survival. 

Charles Darwin is trying to explain the diversity of world, as he found each specie has many different kinds like monkeys are more than 200 types and bats of 1000 types and each specie have something related to other and at the same time something different from others. He wants to see how this is happening in the world. Therefore, he travelled, observed, and made some hypothesis and after many years, he was able to prove how nature is changing.  

Some of the points are discussed here:  
 
### Evolution 

Each new generation produce more offspring than the previous one but not all of them are able to survive. Only those offspring having best inheritance behavior are able to survive and move towards the next generation and by this behavior each new upcoming generation is better than then their ancestors and these modification leads to the best survival of each generation. 

Like a turtle having a peak on its shell can survive better than a turtle having no peak in deserts and this is also the reason there are many kinds in each specie. 

Those individuals with heritable traits better suited to the environment will survive 

- According to the **biological species concept**, organisms belong to the same species if they can interbreed to produce viable, fertile offspring. 
- Species are separated from one another by **prezygotic** and **postzygotic** barriers, which prevent mating or the production of viable, fertile offspring. 
- **Speciation** is the process by which new species form. It occurs when groups in a species become reproductively isolated and diverge. 
- In **allopatric speciation**, groups from an ancestral population evolve into separate species due to a period of geographical separation. 
- In **sympatric speciation**, groups from the same ancestral population evolve into separate species without any geographical separation. 



## **Model** 

In this model, we find the resemblance of every individual with other individuals and observe, how much they are related to each other. Firstly, we have to initialize some initial population and with the method of natural selection, we move towards the best fit. The initial population moves toward the survival of fittest by “**crossover and mutation**”.  

In order to test our model we are given two images. A single image (size (35, 29)) considered as a unit cell and a group image (size (512, 1024)) considered as a population. Each image is a 2D grayscale image.  We have to initialize some random population of the same size as our unit cell from group image and by correlation we found the resemblance of that image. After finding the relation of each individual we create some new generation by cross over and mutation. Each new generation should be better than the previous one and by this evolution each upcoming offspring move towards the best fit or best match that is closely 

resemble to given image or unit cell.

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/009.jpeg)

##  Application 

This application give the detailed information about the scientific logic we extracted and implemented from Darwin’s Theory. This application is based on template matching technique with a scientific approach. 

### Import Image 

First step was to import the image and convert the image into 2D matrixes. We used python library matplot to import and convert the image in 2D matrix format in which each point indicate a pixel on each x and y coordinates. 

### Slicing 

Now the next step was to divide the large image into equal parts of smaller image by taking random points. In order to do that we generate some random x and y coordinates and slice the images having width and length equal to smaller image. The edge point in generating the random number was to minus the width and length of smaller images so that the coordinates don’t get outside of large image. 

Large image (512, 1024) small image (35, 29) minus coordinates of small image from large image and generate random numbers. 

### Initialization 

Now the count of random numbers will be the initial population. Initially we set the count to 50 and 100 and sometime even 10000 after reading some article we get to the conclusion that initial population should be max 40 or 50.But at 50 initial population it does not give result of 0.9 or 0.8 correlation even after long time 

After initializing the population, we checked the correlation between random population and the given image. For correlation we implemented the Peterson correlation method. In order to optimize the code we used python numpy array 

to find correlation. It greatly increase the efficiency of computation 30 to 50 times  

### Sorting 

After finding the correlation, we sort the fitness value in reverse order so that we get the best fitness at top. After that, we convert the top two values into binary number and concatenate them. 

### Crossover and Mutation 

Now the most important step is crossover and mutation. We tried to implement different logics here. Initially we were making crossover and mutation of all the parents and discarding the previous one and initializing the new generation. In mutation we mute each x and y coordinate. Another changing was to mutate least significant bit and most significant bit but both of these haven’t given the desired result. After reading an article we get to know that crossover percentage is 95 and mutation percentage is 0.5 so we moved towards this method but still we haven’t get the desired result mean the increasing curve in graphical representation. 

### Termination 

This procedure repeated until we reach some stopping criteria as if we get 0.9 correlation or any other threshold that we have fixed to stop.  

### Testing’s 

We have tried to implement Darwin’s logic in our algorithm to find the best result but were not able to do that completely. Our task was that each new generation should be better than the previous one and move towards the actual points of small image. The graphical representation that was expected was a straight up curve. However, we concluded that the method of randomization in crossover and mutation is leading us to different direction. Another assumption is that there are also many other points which are closely related to our small image so the graph will not be a straight line. Some of the result given below will prove that.  We get the result at 0.6 correlation but not at 0.79 so according to me graph will not have a straight up curve. We even get 0.9 result if we increase the population to 10000 initial points. After some more experiments I get to conclusion that increasing the population is giving faster result and accurate results at 1000 population but at population of 50 I don’t get any result even after a long time.  

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/010.png)

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/011.jpeg)

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/012.png)

After certain experiments we get to know that correlation was being repeated due to cross over and mutation. It was occurring due to same values of x and y so we check the values if they are same we change them randomly. It greatly help us to get the result 

![](https://github.com/Zia-Ur-Rehman1/Evoltiobary_Algorithm/blob/main/images/013.jpeg)

Conclusion 

After certain different approches we get to conclusion that we can only get straight curve just by luck.For the time being we cannot be sure that our every new genartion will be better thtan the previous one. Another assumption is that this can be done by some cahnging in crossover and mutation. This project also help us to understand how logics of nature can be implemented and how much helpful It can be.  

References 

1. www.livescience.com/474-controversy-evolution-works.html 
1. www.khanacademy.org/science/ap-biology/natural-selection/speciation 
