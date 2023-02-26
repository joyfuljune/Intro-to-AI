<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="notebook-界面">notebook 界面</h1>
<p>创建新的 notebook 时，你会看到如下所示的界面：</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/new-notebook.png" alt="空白文件" style="width: 500px; height: 250px;" class="img img-fluid">
    <figcaption class="figure-caption">
      空白文件
    </figcaption>
  </figure>
</div>
</div>

<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>请随意尝试和四处浏览一下。</p>
<p>你会看到外框为绿色的一个小方框。它称为<em>单元格</em>。单元格是你编写和运行代码的地方。你也可以更改其类型，以呈现 Markdown（一种常用于编写 Web 内容的格式化语法）。我会在后面更详细地介绍 Markdown。在工具栏中点击“Code”，将其改为 Markdown，然后改回来。小型的播放按钮用于运行单元格，而向上和向下的箭头用于上下移动单元格。</p>
</div>
</div>

<figure class="figure">
  <img src="img/02. Notebook+Interface-KkAuoUpqzJs.gif" alt="hello world" style="max-width:60%; max-height:60%;" class="img img-fluid">
      <figcaption class="figure-caption">
        hello world
      </figcaption>
</figure>
                      


<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>运行代码单元格时，单元格下方会显示输出。单元格还会被编号（左侧会显示 <code>In [1]:</code>）。这能让你知道运行的代码和运行顺序（如果运行了多个单元格的话）。在 Markdown 模式下运行单元格会将 Markdown 呈现为文本。</p>
<h2 id="工具栏">工具栏</h2>
<p>从左侧开始，工具栏上的其他控件是：</p>
<ul>
<li>软盘符号表示“保存”。请记得保存 notebook！</li>
<li><code>+</code> 按钮用于创建新的单元格</li>
<li>然后是用于剪切、复制和粘贴单元格的按钮。</li>
<li>运行、停止、重新启动内核</li>
<li>单元格类型：代码、Markdown、原始文本和标题</li>
<li>命令面板（见下文）</li>
<li>单元格工具栏，提供不同的单元格选项（例如将单元格用作幻灯片）</li>
</ul>
<h3 id="命令面板">命令面板</h3>
<p>小键盘符号代表命令面板。点击它会弹出一个带有搜索栏的面板，供你搜索不同的命令。这能切实帮助你加快工作速度，因此你将无需使用鼠标翻查各个菜单。你只需打开命令面板，然后键入要执行的操作。例如，如果要合并两个单元格：</p>
</div>
</div>
<figure class="figure">
  <img src="img/02. Command+Palette-xY4LhuW8xx0.gif" alt="commande palette" style="max-width:60%; max-height:60%;" class="img img-fluid">
        <figcaption class="figure-caption">
                合并代码行
                      </figcaption>
                      </figure>

<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="更多事项">更多事项</h2>
<p>顶部显示了标题。点击它可以将 notebook 重命名。</p>
<p>右侧是内核类型（在我的例子中是 Python 3），旁边是一个小圆形。在内核运行单元格时，会填充这个小圆形。对于大多数快速运行的操作，并不会填充它。它是一个小型指示器，在代码会运行较久时让你知道其实际是在运行中的。</p>
<p>工具栏包含了保存按钮，但 notebook 也会定期自动保存。标题右侧会注明最近一次的保存。你可以使用保存按钮手动进行保存，也可以按键盘上的 <code>Esc</code>，然后按 <code>s</code>。按 <code>Esc</code> 键会变为命令模式，而 <code>s</code> 是“保存”的快捷键。我会在后面介绍命令模式和快捷键。</p>
<p>在“File”（文件）菜单中，你可以选择多种格式进行 notebook 的下载。通常，你会希望将它作为 HTML 文件下载，以便与不使用 Jupyter 的其他人共享。也可以将 notebook 作为普通的 Python 文件下载，此时所有代码都会像平常一样运行。要在博客或文档中使用 notebook，<a href="https://daringfireball.net/projects/markdown/" rel="noopener noreferrer" target="_blank">Markdown</a> 和 <a href="http://docutils.sourceforge.net/rst.html" rel="noopener noreferrer" target="_blank">reST</a> 格式很合适。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/notebook-download.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">另存为
    </figcaption>
  </figure>
</div>
</div>
<div class="divider"></div>
          </div>


<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="jupyter-notebook-是什么？">Jupyter notebook 是什么？</h1>
<p>Jupyter notebook 是一种 Web 应用，能让用户将说明文本、数学方程、代码和可视化内容全部组合到一个易于共享的文档中。例如，不久前我共享了我最爱的一个 Jupyter notebook ，它分析了 <a href="https://www.ligo.caltech.edu/news/ligo20160211" rel="noopener noreferrer" target="_blank">LIGO 实验</a>探测到的<a href="https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html" rel="noopener noreferrer" target="_blank">两个碰撞的黑洞所发出的引力波</a>。你可以下载数据，运行 notebook 中的代码，重复整个分析，实际上等于你自己探测引力波！</p>
<p>Jupyter Notebook 已迅速成为处理数据的必备工具。其用途包括<a href="http://nbviewer.jupyter.org/github/jmsteinw/Notebooks/blob/master/IndeedJobs.ipynb" rel="noopener noreferrer" target="_blank">数据清理和探索</a>、可视化、<a href="http://nbviewer.jupyter.org/github/masinoa/machine_learning/blob/master/04_Neural_Networks.ipynb" rel="noopener noreferrer" target="_blank">机器学习</a>和<a href="http://nbviewer.jupyter.org/github/tdhopper/rta-pyspark-presentation/blob/master/slides.ipynb" rel="noopener noreferrer" target="_blank">大数据分析</a>。我为我的个人博客创建了<a href="https://github.com/mcleonard/blog_posts/blob/master/body_fat_percentage.ipynb" rel="noopener noreferrer" target="_blank">一个 notebook 示例</a>，它展示了 notebook 的许多特点。这项工作通常在终端中完成，也即使用普通的 Python shell 或 IPython 完成。可视化在单独的窗口中进行，而文字资料以及各种函数和类脚本包含在独立的文档中。但是，notebook 能将这一切集中到一处，让用户一目了然。</p>
<p>GitHub 上也直接支持 Jupyter notebook 的渲染。借助此出色的功能，你可以轻松地共享工作。<a href="http://nbviewer.jupyter.org/" rel="noopener noreferrer" target="_blank">http://nbviewer.jupyter.org/</a> 也会提供 GitHub 代码库中的 notebook ，以及存储在其他地方的 notebook。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="文学化编程">文学化编程</h2>
<p>notebook 是 Donald Knuth 在 1984 年提出的<a href="http://www.literateprogramming.com/" rel="noopener noreferrer" target="_blank">文字表达化编程</a>的一种形式。在文字表达化编程中，直接在代码旁写出叙述性文档，而不是另外编写单独的文档。用 Donald Knuth 的话来说：</p>
<blockquote>
  <p>让我们集中精力向人们解释我们希望计算机做什么，而不是指示计算机做什么。</p>
</blockquote>
<p>归根到底，代码是写给人看到，不是写给计算机看的。notebook 恰恰提供了这种能力。你能够直接在代码旁写出叙述性文档。这不仅对阅读 notebook 的人很有用，而且对你将来回头分析代码也很有用。</p>
<p>说点题外话：最近，文字表达化编程这个概念已经发展成为一门完整的编程语言，即 <a href="http://www.witheve.com/" rel="noopener noreferrer" target="_blank">Eve</a>。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="notebook-如何工作">notebook 如何工作</h2>
<p>Jupyter notebook 源自 Fernando Perez 发起的 <a href="https://ipython.org/" rel="noopener noreferrer" target="_blank">IPython 项目</a>。IPython 是一种交互式 shell，与普通的 Python shell 相似，但具有一些很好的功能（例如语法高亮显示和代码补全）。最初，notebook 的工作方式是，将来自 Web 应用（你在浏览器中看到的 notebook）的消息发送给 IPython 内核（在后台运行的 IPython 应用程序）。内核执行代码，然后将结果发送回 notebook。当前架构与之相似，具体见下图。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/notebook-components.png" alt="摘自 [Jupyter 文档](https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html)" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>摘自 <a href="https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html" rel="noopener noreferrer" target="_blank">Jupyter 文档</a></p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>核心是 notebook 的服务器。你通过浏览器连接到该服务器，而 notebook 呈现为 Web 应用。你在 Web 应用中编写的代码通过该服务器发送给内核，内核运行代码，并将结果发送回该服务器。之后，任何输出都会返回到浏览器中。保存 notebook 时，它将作为 JSON 文件（文件扩展名为 <code>.ipynb</code>）写入到该服务器中。</p>
<p>此架构的一个优点是，内核无需运行 Python。由于 notebook 和内核分开，因此可以在两者之间发送任何语言的代码。例如，早期的两个非 Python 内核分别是 <a href="https://www.r-project.org/" rel="noopener noreferrer" target="_blank">R</a> 语言和 <a href="http://julialang.org/" rel="noopener noreferrer" target="_blank">Julia</a> 语言。使用 R 内核时，用 R 编写的代码将发送给执行该代码的 R 内核，这与在 Python 内核上运行 Python 代码完全一样。IPython notebook 已被改名，因为 notebook 变得与编程语言无关。新的名称 <strong>Jupyter</strong> 由 <strong>Ju</strong>lia、<strong>Pyt</strong>hon 和 <strong>R</strong> 组合而成。如果有兴趣，不妨看看<a href="https://github.com/jupyter/jupyter/wiki/Jupyter-kernels" rel="noopener noreferrer" target="_blank">可用内核的列表</a>。</p>
<p>另一个优点是，你可以在任何地方运行 notebook 服务器，并且可通过互联网访问服务器。通常，你会在存储所有数据和 notebook 文件的自有计算机上运行服务器。但是，你也可以在远程计算机或云实例（如 Amazon 的 EC2）上<a href="http://jupyter-notebook.readthedocs.io/en/latest/public_server.html" rel="noopener noreferrer" target="_blank">设置服务器</a>。之后，你就可以在世界上任何地方通过浏览器访问 notebook。</p>
</div>

</div>
<div class="divider"></div>
          </div>
          



<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="启动-notebook-服务器">启动 notebook 服务器</h1>
<p>要启动 notebook 服务器，请在终端或控制台中输入 <code>jupyter notebook</code>。服务器会在你运行此命令的目录中启动。这意味着任何 notebook 文件都会保存在该目录下。你通常希望在 notebook 文件所在的目录中启动服务器，不过你也可以在文件系统中导航到 notebook 文件所在的位置。</p>
<p>运行此命令时（请自己试一下！），服务器主页会在浏览器中打开。默认情况下，notebook 服务器的运行地址是 <code>http://localhost:8888</code>。该地址的含义是：<code>localhost</code> 表示你的计算机，而 <code>8888</code> 是服务器的通信端口。只要 notebook 服务器仍在运行，你随时都能通过在浏览器中输入 http://localhost:8888 返回到 web 页面中。</p>
<p>如果同时启动了另一个 notebook 服务器，新服务器会尝试使用端口 <code>8888</code>，但由于此端口已被占用，因此新服务器会在端口 <code>8889</code> 上运行。之后，你可以通过 <code>http://localhost:8889</code> 连接到新服务器。每个额外的 notebook 服务器都会像这样增大端口号。</p>
<p>如果你尝试启动自己的服务器，它应类似以下所示：</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/notebook-server.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">空白目录
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>你可能会看到上面列表中的一些文件和文件夹，具体取决于你在哪里启动服务器。</p>
<p>在右侧，你可以点击“New”（新建），创建新的 notebook、文本文件、文件夹或终端。“Notebooks”下的列表显示了你已安装的内核。由于我在 Python 3 环境中运行服务器，因此列出了 Python 3 内核。你在这里看到的可能是 Python 2。我还安装了用于 Scala 2.10 和 2.11 的内核，因此它们出现在列表中。</p>
<p>如果在 conda 环境中运行 Jupyter notebook 服务器，则你还能选择环境中任何其他的内核（见下图）。要创建新的 notebook，请点击你要使用的内核。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/conda-environments.png" alt="Jupyter 中的 Conda 环境" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>Jupyter 中的 Conda 环境</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>顶部的选项卡是 <em>Files</em>（文件）、<em>Running</em>（运行）和 <em>Cluster</em>（集群）。<em>Files</em>（文件）显示当前目录中的所有文件和文件夹。点击 <em>Running</em>（运行）选项卡会列出所有正在运行的 notebook。可以在该选项卡中管理这些 notebook。</p>
<p>过去，在 <em>Clusters</em>（集群）中创建多个用于并行计算的内核。现在，这项工作已经由 <a href="https://ipyparallel.readthedocs.io/en/latest/intro.html" rel="noopener noreferrer" target="_blank">ipyparallel</a> 接管，因此该选项卡如今用处不多。</p>
<p>如果在 conda 环境中运行 notebook 服务器，则你还能访问以下所示的“Conda”选项卡。<br>
（需要在terminal中安装“Conda”选项卡，语句为conda install jupyter notebook nb_conda）</p>
<p>可以通过该选项卡管理 Jupyter 中的环境。你可以执行多种操作，例如创建新的环境、安装包、更新包、导出环境。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/conda-tab.png" alt="Jupyter 中的 Conda 选项卡" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>Jupyter 中的 Conda 选项卡</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h3 id="关闭-jupyter">关闭 Jupyter</h3>
<p>通过在服务器主页上选中 notebook 旁边的复选框，然后点击“Shutdown”（关闭），你就可以关闭各个 notebook。但是，在这样做之前，请确保你保存了工作！否则，在你上次保存后所做的任何更改都会丢失。下次运行 notebook 时，你还需要重新运行代码。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/notebook-shutdown.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">关闭notebook
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>通过在终端中按两次 Ctrl + C，可以关闭整个服务器。再次提醒，这会立即关闭所有运行中的 notebook，因此，请确保你保存了工作！</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/server-shutdown.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">关闭服务器
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div>
          </div>
          
<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="markdown-单元格">Markdown 单元格</h1>
<p>如前所述，单元格也可用于以 Markdown 编写的文本。Markdown 是格式化语法，可让你加入链接、将文本样式设为粗体或斜体和设置代码格式。像代码单元格一样，按 <strong>Shift + Enter</strong> 或 <strong>Ctrl + Enter</strong> 可运行 Markdown 单元格，这会将 Markdown 呈现为格式化文本。加入文本可让你直接在代码旁写出叙述性文档，以及为代码和思路编写文档。</p>
<p>你可以<a href="https://daringfireball.net/projects/markdown/basics" rel="noopener noreferrer" target="_blank">在此处查找文档</a>，但我会提供简短的入门文档。</p>
<h2 id="标题">标题</h2>
<p>要编写标题，可在文本前放置井号，即 <code>#</code>（英文读作 pound、hash 或 <a href="http://www.worldwidewords.org/weirdwords/ww-oct1.htm" rel="noopener noreferrer" target="_blank">octothorpe</a>）。一个 <code>#</code> 呈现为 <code>h1</code> 标题，两个 <code>#</code> 是 h2 标题，依此类推。类似以下所示：</p>
<pre><code class="[Markdown] language-[Markdown]"># Header 1
## Header 2
### Header 3</code></pre>
<p>呈现为</p>
<h1 id="header-1">Header 1</h1>
<h2 id="header-2">Header 2</h2>
<h3 id="header-3">Header 3</h3>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="链接">链接</h2>
<p>要在 Markdown 中添加链接，请在文本两侧加上方括号，并在 URL 两侧加上圆括号，例如：<code>[南京工业大学浦江学院教务处](https://my.njpji.cn)</code> 表示指向 <a href="https://my.njpji.cn" rel="noopener noreferrer" target="_blank">教务处网址</a> 的链接。</p>
<h2 id="强调效果">强调效果</h2>
<p>可以使用星号或下划线（<code>*</code> 或 <code>_</code>）来表示粗体或斜体，从而添加强调效果。对于斜体，在文本两侧加上一个星号或下划线，例如 <code>_斜体_</code> 或 <code>*斜体*</code> 会呈现为 <em>斜体</em>。</p>
<p>粗体文本使用两个符号，例如 <code>**加粗**</code> 或 <code>__加粗__</code> 会呈现为 <strong>加粗</strong>。</p>
<p>只要在文本两侧使用相同的符号，星号和下划线的作用都一样。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="代码">代码</h2>
<p>可以通过两种不同的方式显示代码，一种是与文本内联，另一种是将代码块与文本分离。要将代码变为内联格式，请在文本两侧加上反撇号。例如，<code>`string.punctuation`</code> 会呈现为 <code>string.punctuation</code>。</p>
<p>要创建代码块，请另起一行并用三个反撇号（一般在键盘数字 1 左边）将文本包起来：</p>
<pre><code>```
import requests
response = requests.get('https://www.udacity.com')
```</code></pre>
<p>或者将代码块的每一行都缩进四个空格。</p>
<pre><code class="python language-python">import requests
response = requests.get('https://www.udacity.com')</code></pre>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="数学表达式">数学表达式</h2>
<p>在 Markdown 单元格中，可以使用 <a href="https://www.latex-project.org/" rel="noopener noreferrer" target="_blank">LaTeX</a> 符号创建数学表达式。notebook 使用 MathJax 将 LaTeX 符号呈现为数学符号。要启动数学模式，请在 LaTeX 符号两侧加上美元符号（例如 <code>$y = mx + b$</code>），以创建内联的数学表达式。对于数学符号块，请使用两个美元符号：</p>
<pre><code>$$
y = \frac{a}{b+c}
$$</code></pre>
<p>此功能的确很有用，因此，如果你没有用过 LaTeX，<a href="https://blog.csdn.net/GarfieldEr007/article/details/51646604" rel="noopener noreferrer" target="_blank">请阅读这篇入门文档</a>，它介绍了如何使用 LaTeX 来创建数学表达式。</p>
</div>
</div>

  <figure class="figure">
      <img src="img/unnamed-220107-0.gif" alt="" class="img img-fluid">
          <figcaption class="figure-caption">markdown语法
              </figcaption>
                </figure>

<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="小结">小结</h2>
<p>在编写 Markdown 时，可以参考这个<a href="https://blog.csdn.net/u014061630/article/details/81359144" rel="noopener noreferrer" target="_blank">速查指南</a>。我建议使用 Markdown 单元格，与使用一堆代码块相比，这使 notebook 变得更易于阅读。</p>
</div>

</div>
<div class="divider"></div>
          </div>          
 
 
<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="magic-关键字">Magic 关键字</h1>
<p>Magic 关键字是可以在单元格中运行的特殊命令，能让你控制 notebook 本身或执行系统调用（例如更改目录）。例如，在 notebook 中可以使用 <code>%matplotlib</code> 将 matplotlib 设置为以交互方式工作。</p>
<p>Magic 命令的前面带有一个或两个百分号（<code>%</code> 或 <code>%%</code>），分别对应行 Magic 命令和单元格 Magic 命令。行 Magic 命令仅应用于编写 Magic 命令时所在的行，而单元格 Magic 命令应用于整个单元格。</p>
<p><strong>注意：</strong>这些 Magic 关键字是特定于普通 Python 内核的关键字。如果使用其他内核，这些关键字很有可能无效。</p>
<h2 id="代码计时">代码计时</h2>
<p>有时候，你可能要花些精力优化代码，让代码运行得更快。在此优化过程中，必须对代码的运行速度进行计时。可以使用 Magic 命令 <code>timeit</code> 测算函数的运行时间，如下所示：</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/magic-timeit.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">函数计时
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>如果要测算整个单元格的运行时间，请使用 <code>%%timeit</code>，如下所示：</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/magic-timeit2.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">代码计时     
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="在-notebook-中嵌入可视化内容">在 notebook 中嵌入可视化内容</h2>
<p>如前所述，notebook 允许你将图像与文本和代码一起嵌入。这在你使用 <code>matplotlib</code> 或其他绘图包创建可视化内容时最为有用。在 notebook 中可以使用 <code>%matplotlib</code> 将 <code>matplotlib</code> 设置为以交互方式工作。默认情况下，图形呈现在各自的窗口中。但是，你可以通过命令传递参数，以选择特定的<a href="http://matplotlib.org/faq/usage_faq.html#what-is-a-backend" rel="noopener noreferrer" target="_blank">“后端”</a>（呈现图像的软件）。要直接在 notebook 中呈现图形，应将通过命令 <code>%matplotlib inline</code> 内联后端一起使用。</p>
<blockquote>
  <p><strong>提示：</strong>在分辨率较高的屏幕（例如 Retina 显示屏）上，notebook 中的默认图像可能会显得模糊。可以在 <code>%matplotlib inline</code> 之后使用 <code>%config InlineBackend.figure_format = 'retina'</code> 来呈现分辨率较高的图像。</p>
</blockquote>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/magic-matplotlib.png" alt="notebook 中的图形示例" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>notebook 中的图形示例</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <h2 id="在-notebook-中进行调试">在 notebook 中进行调试</h2>
<p>对于 Python 内核，可以使用 Magic 命令 <code>%pdb</code> 开启交互式调试器。出错时，你能检查当前命名空间中的变量。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/magic-pdb.png" alt="在 notebook 中进行调试" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>在 notebook 中进行调试</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>在上图中，可以看到我尝试对字符串求和，这造成了错误。调试器指出了该错误，并提示你检查代码。</p>
<p>要详细了解 <code>pdb</code>，请阅读<a href="https://docs.python.org/3/library/pdb.html" rel="noopener noreferrer" target="_blank">此文档</a>。要退出调试器，在提示符中输入 <code>q</code> 即可。</p>
<h2 id="补充读物">补充读物</h2>
<p>Magic 命令还有很多，我只是介绍了你将会用得最多的一些命令。要了解更多信息，请查看<a href="http://ipython.readthedocs.io/en/stable/interactive/magics.html" rel="noopener noreferrer" target="_blank">此列表</a>，它列出了所有可用的 Magic 命令。</p>
</div>
</div>
<div class="divider"></div>
          </div>
          
          
          
<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="快捷键">快捷键</h1>
<p>notebook 自带一组快捷键，能让你使用键盘与单元格交互，而无需使用鼠标和工具栏。熟悉这些快捷键需要花费一点时间，但如果能熟练掌握，将大大加快你在 notebook 中的工作速度。要详细了解这些快捷键和练习它们的用法，请在下面下载 notebook <a href="https://raw.githubusercontent.com/udacity/cn-deep-learning/master/tutorials/jupyter-notebook-tutorial/keyboard-shortcuts.ipynb" rel="noopener noreferrer" target="_blank">Keyboard Shortcuts</a>。再次提醒，浏览器可能会尝试打开它，但请将它保存到计算机中。请右击链接并选择“链接另存为…”。</p>
</div>

</div>
<div class="divider"></div>
          </div>
          
          
          
          
<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="转换-notebook">转换 notebook</h1>
<p>Notebook 只是扩展名为 <code>.ipynb</code> 的大型 <a href="http://www.json.org/" rel="noopener noreferrer" target="_blank">JSON</a> 文件。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/notebook-json.png" alt="在文本编辑器中打开的 notebook 文件显示 JSON 数据" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>在文本编辑器中打开的 notebook 文件显示 JSON 数据</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>由于 notebook 是 JSON 文件，因此，可以轻松将其转换为其他格式。Jupyter 附带了一个名为 <code>nbconvert</code> 的实用程序，可将 notebook 转换为 HTML、Markdown、幻灯片等格式。</p>
<p>例如，要将 notebook 转换为 HTML 文件，请在终端中使用</p>
<pre><code class="bash language-bash">jupyter nbconvert --to html notebook.ipynb</code></pre>
<p>我们也可以在notebook界面中点击<code>File</code>，在弹出的菜单中点击<code>Download as</code>，之后选择我们需要转换的格式。</p>
<p><img src="img/unnamed-220122-0.gif"></p>
<p>要将 notebook 与不使用 notebook 的其他人共享，转换为 HTML 很有用。而要在博客和其他接受 Markdown 格式化的文本编辑器中显示 notebook，Markdown 很合适。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/nbconvert-example.png" alt="" class="img img-fluid">
    <figcaption class="figure-caption">
      类型转换
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>像平常一样，要详细了解 <code>nbconvert</code>，请阅读相关<a href="https://nbconvert.readthedocs.io/en/latest/usage.html" rel="noopener noreferrer" target="_blank">文档</a>。</p>
</div>

</div>
<div class="divider"></div>
          </div>
          
          
<div class="col-12">
<div class="ud-atom">
  <h3></h3>
<div>
<h1 id="代码单元格">代码单元格</h1>
  <p>notebook 中的大部分工作均在代码单元格中完成。这是编写和执行代码的地方。在代码单元格中可以执行多种操作，例如编写代码、给变量赋值、定义函数和类、导入包等。在一个单元格中执行的任何代码在所有其他单元格中均可用。</p>
  <p>请在下面或当前目录下载此 notebook <a href="working-with-code-cells.ipynb" rel="noopener noreferrer" target="_blank">Working With Code Cells</a>，然后从你自己的 notebook 服务器运行它（在你的终端中，转到包含此 notebook 文件的目录，然后输入 <code>jupyter notebook</code>）。浏览器可能会尝试不下载就打开此 notebook 文件。如果是这样，请右击链接并选择“链接另存为…”。</p>
</div>
</div>
<div class="divider"></div>
</div>       
          
<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="创建幻灯片">创建幻灯片</h1>
<p>通过 notebook 创建幻灯片是我最爱的功能之一，<a href="http://nbviewer.jupyter.org/format/slides/github/jorisvandenbossche/2015-PyDataParis/blob/master/pandas_introduction.ipynb#/" rel="noopener noreferrer" target="_blank">你可以在浏览器中直接打开它</a>，它介绍了用于处理数据的 Pandas。</p>
<p>在 notebook 中创建幻灯片的过程像平常一样，但需要指定作为幻灯片的单元格和单元格的幻灯片类型。在菜单栏中，点击“View”（视图）&gt;“Cell Toolbar”（单元格工具栏）&gt;“Slideshow”（幻灯片），以便在每个单元格上弹出幻灯片单元格菜单。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/slides-cell-toolbar-menu.png" alt="打开单元格的幻灯片工具栏" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>打开单元格的幻灯片工具栏</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>这会在每个单元格上显示一个下拉菜单，让你选择单元格在幻灯片中的显示方式。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/slides-choose-slide-type.png" alt="选择幻灯片类型" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>选择幻灯片类型</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p><strong>Slides</strong>（幻灯片）是你从左向右移动的完整幻灯片。按向上或向下的箭头时，<strong>Sub-slides</strong>（子幻灯片）会出现在幻灯片中。<strong>Fragments</strong>（片段）最初是隐藏的，在你按下按钮时会出现。选择Skip（忽略）会在幻灯片中忽略该单元格，而选择 <strong>Notes</strong>（备注）会将为演讲者保留备注。</p>
<h2 id="运行幻灯片">运行幻灯片</h2>
<p>要通过 notebook 文件创建幻灯片，需要使用 <code>nbconvert</code>：</p>
<pre><code class="bash language-bash">    jupyter nbconvert notebook.ipynb --to slides</code></pre>
<p>这只是将 notebook 转换为幻灯片必需的文件，你需要向其提供 HTTP 服务器才能真正看到演示文稿。</p>
<p>要转换它并立即看到它，请使用</p>
<pre><code class="bash language-bash">jupyter nbconvert notebook.ipynb --to slides --post serve</code></pre>
<p>这会在浏览器中打开幻灯片，让你可以演示它。</p>
</div>

</div>
<div class="divider"></div>
          </div>          


