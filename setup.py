from setuptools import setup, find_packages

setup(
    name='md_streamer',
    version='0.0.3',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'mistune',
    ],
    author='Gangchain',
    author_email='gaganjot1872@gmail.com',
    description='streaming markdown to html converter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GangChain/md_streamer-py',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.9',
)