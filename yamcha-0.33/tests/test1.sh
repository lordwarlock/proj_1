#!/bin/sh

make -f ../training/Makefile CORPUS=train.data MODEL=tmp YAMCHA=../src/yamcha TOOLDIR=../libexec train
echo "Evaluating test.data,  please wait ..."
../src/yamcha -m tmp.model < test.data > tmp.result
perl ../libexec/conlleval.pl < tmp.result
perl ../libexec/mkmodel -t ../libexec -e tmp.txtmodel.gz tmp.model
../src/yamcha -m tmp.model < test.data > tmp.result
perl ../libexec/conlleval.pl < tmp.result



	
