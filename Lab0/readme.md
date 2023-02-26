<div class="col-12">
            <div class="ud-atom">
  <h3><p>安装说明</p></h3>
  <div>
  <h1 id="安装-anaconda">安装 Anaconda</h1>
<p>Anaconda 可用于 Windows、Mac OS X 和 Linux。可以在 <a href="https://www.anaconda.com/download/" rel="noopener noreferrer" target="_blank">https://www.anaconda.com/download/</a> 上找到安装程序和安装说明。</p>
<p>如果计算机上已经安装了 Python，这不会有任何影响。实际上，脚本和程序使用的默认 Python 是 Anaconda 附带的 Python。</p>
<p>选择 Python 3.12 版本（你也可以根据具体的需要选择 Python 2 的版本）。此外，如果是 64 位操作系统，则选择 64 位安装程序，否则选择 32 位安装程序。选择下载合适的版本，并继续进行安装！</p>
<p>完成安装后，会自动进入默认的 conda 环境，而且所有包均已安装完毕，如下面所示。可以在终端或命令提示符中键入 <code>conda list</code>，以查看你安装的内容。</p>
<p>在 Windows 上，会随 Anaconda 一起安装一批应用程序：</p>
<ul>
<li>Anaconda Navigator，它是用于管理环境和包的 GUI</li>
<li>Anaconda Prompt 终端，它可让你使用命令行界面来管理环境和包</li>
<li>Spyder，它是面向科学开发的 IDE</li>
</ul>
<p>为了避免报错，推荐在默认环境下更新所有的包。打开 Anaconda Prompt （或者 Mac 下的终端），键入：</p>
<pre><code>conda upgrade --all</code></pre>
<p>并在提示是否更新的时候输入 y（Yes）以便让更新继续。初次安装下的软件包版本一般都比较老旧，因此提前更新可以避免未来不必要的问题。</p>
<p>在本课的余下部分，强烈建议以这种方式开始使用 Anaconda，之后再根据需要使用 GUI。</p>
</div>
</div>
<div class="divider"></div>
          </div>
 
 <div class="col-12">
            <div class="ud-atom">
  <h3><p>序言</p></h3>
  <div>
  <h1 id="anaconda">Anaconda</h1>
<p>如何使用 <a href="https://www.continuum.io/why-anaconda" rel="noopener noreferrer" target="_blank">Anaconda</a> 来管理 Python 所用的包和环境。Anaconda 能让你在数据科学的工作中轻松安装经常使用的程序包。你还将使用它创建虚拟环境，以便更轻松地处理多个项目。Anaconda 简化了工作流程，并且解决了多个包和 Python 版本之间遇到的大量问题。</p>
<p>Anaconda 实际上是一个软件发行版，它附带了 <code>conda</code>、Python 和 150 多个科学包及其依赖项。应用程序 <code>conda</code> 是包和环境管理器。Anaconda 的下载文件比较大（约 500 MB），因为它附带了 Python 中最常用的数据科学包。如果只需要某些包，或者需要节省带宽或存储空间，也可以使用 <a href="https://conda.io/miniconda.html" rel="noopener noreferrer" target="_blank">Miniconda</a> 这个较小的发行版（仅包含 <code>conda</code> 和 Python）。但你仍可以使用 <code>conda</code> 来安装任何可用的包，只是它自身没有附带这些包而已。</p>
<p><code>conda</code> 只能通过命令行来使用。因此，如果你觉得它很难用，可以参考<a href="https://learn.microsoft.com/zh-cn/windows/terminal/command-line-arguments?tabs=windows" target="_blank">面向 Windows 的命令提示符教程</a>，或者学习面向 OSX/Linux 用户的命令行基础知识课程。</p>
<p>你可能已经安装了 Python，并且想知道为何还需要 Anaconda。首先， Anaconda 附带了一大批常用数据科学包，因此你可以立即开始处理数据。其次，使用 <code>conda</code> 来管理包和环境能减少将来在处理数据过程中使用到的各种库与版本时遇到的问题。</p>
<h2 id="管理包">管理包</h2>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/conda-install.png" alt="使用 conda 安装 numpy" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>使用 conda 安装 numpy</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>包管理器用于在计算机上安装库和其他软件。你可能已经熟悉 <code>pip</code>，它是 Python 库的默认包管理器。<code>conda</code> 与 <code>pip</code> 相似，不同之处是可用的包以数据科学包为主，而 <code>pip</code> 适合一般用途。与此同时，<code>conda</code> 并非像 <code>pip</code> 那样专门适用于 Python，它也可以安装非 Python 的包。它是支持任何软件的包管理器。也就是说，虽然并非所有的 Python 库都能通过 Anaconda 发行版和 conda 获得，但同时它也支持非 Python 库的获得。在使用 conda 的同时，你仍可以使用 <code>pip</code> 来安装包。</p>
<p>Conda 安装了预编译的包。例如，Anaconda 发行版附带了使用 <a href="https://docs.continuum.io/mkl-optimizations/" rel="noopener noreferrer" target="_blank">MKL 库</a>编译的 Numpy、Scipy 和 Scikit-learn，从而加快了各种数学运算的速度。这些包由发行版的贡献者维护，这意味着它们通常滞后于最新版本。但是，由于有人需要利用这些包来进行系统构建，因此它们往往更为稳定，而且也更便于你使用。</p>
<h2 id="环境">环境</h2>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/conda-create-env.png" alt="使用 conda 创建环境" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>使用 conda 创建环境</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>除了管理包之外，conda 还是虚拟环境管理器。它类似于另外两个很流行的环境管理器，即 <a href="https://virtualenv.pypa.io/en/stable/" rel="noopener noreferrer" target="_blank">virtualenv</a> 和 <a href="https://github.com/yyuu/pyenv" rel="noopener noreferrer" target="_blank">pyenv</a>。</p>
<p>你可以使用conda环境管理器分隔不同项目的包。你常常要使用依赖于某个库的不同版本的代码。例如，你的代码可能使用了 Numpy 中的新功能，或者使用了已删除的旧功能。实际上，不可能同时安装两个 Numpy 版本。你要做的应该是，为每个 Numpy 版本创建一个环境，然后在项目的对应环境中工作。</p>
<p>在应对 Python 2 和 Python 3 时，此问题也会常常发生。你可能会使用在 Python 3 中不能运行的旧代码，以及在 Python 2 中不能运行的新代码。同时安装两个版本可能会造成许多混乱和错误，而创建独立的环境会好很多。</p>
<p>你也可以将环境中的包列表导出为文件，然后将该文件与代码打包在一起。这能让其他人轻松加载代码的所有依赖项。pip 提供了类似的功能，即 <code>pip freeze &gt; requirements.txt</code>。</p>
</div>

</div>
<div class="divider"></div>
          </div>

<div class="col-12">
            <div class="ud-atom">
  <h3></h3>
  <div>
  <h1 id="管理包">管理包</h1>
<p>安装了 Anaconda 之后，管理包是相当简单的。要安装包，请在终端中键入 <code>conda install package_name</code>。例如，要安装 numpy，请键入 <code>conda install numpy</code>。</p>

</video><div class="plyr__poster"></div></div><div class="plyr__captions"></div><button type="button" class="plyr__control plyr__control--overlaid plyr__control--pressed" data-plyr="play" aria-label="Play"><svg role="presentation" focusable="false"><use xlink:href="#plyr-play"></use></svg><span class="plyr__sr-only">Play</span></button></div>
<p>你还可以同时安装多个包。类似 <code>conda install numpy scipy pandas</code> 的命令会同时安装所有这些包。还可以通过添加版本号（例如 <code>conda install numpy=1.10</code>）来指定所需的包版本。</p>
<p>Conda 还会自动为你安装依赖项。例如，<code>scipy</code> 依赖于 <code>numpy</code>，因为它使用并需要 <code>numpy</code>。如果你只安装 <code>scipy</code> (<code>conda install scipy</code>)，则 conda 还会安装 <code>numpy</code>（如果尚未安装的话）。</p>
<p>大多数命令都是很直观的。要卸载包，请使用 <code>conda remove package_name</code>。要更新包，请使用 <code>conda update package_name</code>。如果想更新环境中的所有包（这样做常常很有用），请使用 <code>conda update --all</code>。最后，要列出已安装的包，请使用前面提过的 <code>conda list</code>。</p>
<p>如果不知道要找的包的确切名称，可以尝试使用 <code>conda search search_term</code> 进行搜索。例如，我知道我想安装 <a href="https://www.crummy.com/software/BeautifulSoup/" rel="noopener noreferrer" target="_blank">Beautiful Soup</a>，但我不清楚确切的包名称。因此，我尝试执行 <code>conda search beautifulsoup</code>。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <figure class="figure">
    <img src="img/conda-search-beautifulsoup.png" alt="搜索 beautifulsoup" class="img img-fluid">
    <figcaption class="figure-caption">
      <p>搜索 beautifulsoup</p>
    </figcaption>
  </figure>
</div>


</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <p>它返回可用的 Beautiful Soup 包的列表，并列出了相应的包名称 <code>beautifulsoup4</code>。</p>
</div>

</div>
<div class="divider"></div><div class="ud-atom">
  <h3></h3>
  <div>
  <form>
    <fieldset>
      <legend><p>通过 conda ，你可使用以下哪个命令来安装包 <code>numpy</code> 和 <code>pandas</code>？（多选）</p></legend>
    </fieldset>

    <div>
      <input type="checkbox" value="a1480541673069" name="220072" id="a1480541673069">
      <label for="a1480541673069"><p><code>conda install numpy</code></p></label>
    </div>
    <div>
      <input type="checkbox" value="a1480541700965" name="220072" id="a1480541700965">
      <label for="a1480541700965"><p><code>conda install pandas</code></p></label>
    </div>
    <div>
      <input type="checkbox" value="a1480541709026" name="220072" id="a1480541709026">
      <label for="a1480541709026"><p><code>conda install numpy pandas</code></p></label>
    </div>
  </form>

  <details>
    <summary><strong>SOLUTION:</strong></summary>
    <ul>
      <li>`conda install pandas`</li>
      <li>`conda install numpy pandas`</li>
  </ul>
  </details>
</div>

</div>
<div class="divider"></div>
          </div>
