## Description

计算帕鲁配种最短合成路线

## Usage

pip install -r requirements.txt

python3 love.py <已有帕鲁> <目标帕鲁> <富裕程度>

<富裕程度>是一个int值，一般来讲，越稀有的帕鲁，其ID越大，例如棉悠悠ID是1，空涡龙ID是111，富裕程度是一个手动调参，在计算最短路线的时候只会使用ID不超过<富裕程度>的帕鲁。

## Example
救救，我抓到了一个工匠大师壶小象，怎么配一个工匠大师阿努比斯啊

python3 love.py 壶小象  阿努比斯 80