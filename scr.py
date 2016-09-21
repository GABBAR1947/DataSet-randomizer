#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# GABBAR STUDIOWORKSi
# Copyright © 2016 gabbar1947 <gabbar1947@Rathores-MacBook-Pro.local>
import numpy as np
import os as OS

Data = open('PascalDataTest.txt','r+');
Result = open('results.txt','w');
num_lines = sum(1 for line in open('PascalDataTest.txt'));

#with Data as f:
#    Out = f.readlines()

Out = Data.read().splitlines();

#Result.write(Out[0]);
#Result.write(Out[1]);
#Result.write(Out[2]);
#print(Out);

np.random.shuffle(Out);
Result.write("\n".join(Out));

Data.close();
Result.close();
