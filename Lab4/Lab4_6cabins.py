import ipywidgets as widgets
from IPython.display import display, HTML
import numpy as np


def pred():
    np.set_printoptions(precision=1)
    x = np.array(
        [
            [25, 2, 50, 1, 500],
            [39, 3, 10, 1, 1000],
            [13, 2, 13, 1, 1000],
            [82, 5, 20, 2, 120],
            [130, 6, 10, 2, 600],
            [input1.value, input2.value, input3.value, input4.value, input5.value]
        ]
    )
    y = np.array([127900, 222100, 143750, 268000, 460700, input6.value])
    c = np.linalg.lstsq(x, y, rcond=None)[0]
    result = [input1.value, input2.value, input3.value, input4.value, input5.value] @ c
    return c, result


coeffs, result = pred()

# Define the table HTML string
table_html = """
<table class="e6m5nkm0 css-9vwhni e14yjuwg0">
    <thead>
        <tr>
            <th> </th>
            <th>房屋面积（c1）</th>
            <th>桑拿房大小（c2）</th>
            <th>离水距离（c3）</th>
            <th>洗手间数量（c4）</th>
            <th>离邻居距离(c5)</th>
            <th>实际价格(￥)</th>
            <th>预测价格(￥)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td disabled="" contenteditable="false">1号房</td>
            <td disabled="" contenteditable="false">25</td>
            <td disabled="" contenteditable="false">2</td>
            <td disabled="" contenteditable="false">50</td>
            <td disabled="" contenteditable="false">1</td>
            <td disabled="" contenteditable="false">500</td>
            <td disabled="" contenteditable="false">127,900</td>
            <td disabled="" contenteditable="false">127,900</td>
        </tr>
        <tr>
            <td disabled="" contenteditable="false">2号房</td>
            <td disabled="" contenteditable="false">39</td>
            <td disabled="" contenteditable="false">3</td>
            <td disabled="" contenteditable="false">10</td>
            <td disabled="" contenteditable="false">1</td>
            <td disabled="" contenteditable="false">1,000</td>
            <td disabled="" contenteditable="false">222,100</td>
            <td disabled="" contenteditable="false">222,100</td>
        </tr>
        <tr>
            <td disabled="" contenteditable="false">3号房</td>
            <td disabled="" contenteditable="false">13</td>
            <td disabled="" contenteditable="false">2</td>
            <td disabled="" contenteditable="false">13</td>
            <td disabled="" contenteditable="false">1</td>
            <td disabled="" contenteditable="false">1,000</td>
            <td disabled="" contenteditable="false">143,750</td>
            <td disabled="" contenteditable="false">143,750</td>
        </tr>
        <tr>
            <td disabled="" contenteditable="false">4号房</td>
            <td disabled="" contenteditable="false">82</td>
            <td disabled="" contenteditable="false">5</td>
            <td disabled="" contenteditable="false">20</td>
            <td disabled="" contenteditable="false">2</td>
            <td disabled="" contenteditable="false">120</td>
            <td disabled="" contenteditable="false">268,000</td>
            <td disabled="" contenteditable="false">268,000</td>

        </tr>
        <tr>
            <td disabled="" contenteditable="false">5号房</td>
            <td disabled="" contenteditable="false">130</td>
            <td disabled="" contenteditable="false">6</td>
            <td disabled="" contenteditable="false">10</td>
            <td disabled="" contenteditable="false">2</td>
            <td disabled="" contenteditable="false">600</td>
            <td disabled="" contenteditable="false">460,700</td>
            <td disabled="" contenteditable="false">460,700</td>
        </tr>
        <tr>
            <td disabled="" contenteditable="false">6号房</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{}</td>
            <td disabled="" contenteditable="false">{:.3f}</td>
        </tr>
    </tbody>
</table>""".format(input1.value, input2.value, input3.value, input4.value, input5.value, input6.value, result)

# Display the table
display(HTML(table_html))

table_coeffs = """
    <tbody>
        <tr>
            <th disabled="" contenteditable="false">c1</th>
            <th disabled="" contenteditable="false">c2</th>
            <th disabled="" contenteditable="false">c3</th>
            <th disabled="" contenteditable="false">c4</th>
            <th disabled="" contenteditable="false">c5</th>
        </tr>
        <tr>
            <td disabled="" contenteditable="false">{:.3f}</td>
            <td disabled="" contenteditable="false">{:.3f}</td>
            <td disabled="" contenteditable="false">{:.3f}</td>
            <td disabled="" contenteditable="false">{:.3f}</td>
            <td disabled="" contenteditable="false">{:.3f}</td>
        </tr>
        </tbody>""".format(coeffs[0],coeffs[1],coeffs[2],coeffs[3],coeffs[4])

print('最小二乘法计算系数')
display(HTML(table_coeffs))
