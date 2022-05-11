import argparse
import lxml.etree as et

def parse_args():
    parser = argparse.ArgumentParser(description='Apply xsl')
    parser.add_argument('target', help='Source file')
    parser.add_argument('xsl', help='XSL file')
    parser.add_argument('-o', '--output', required=False, type=str, help='Output file')
    return parser.parse_args()

def save_file(filename, content):
    file = open(filename, 'w')
    filecontent = content.decode('utf-8')
    file.write(filecontent)
    file.close()

def process(target, xsl_file, output):
    print(f'Reading {target}')
    dom = et.parse(target)
    xsl = et.parse(xsl_file)
    transform = et.XSLT(xsl)
    new_dom = transform(dom)
    new_doc = et.tostring(new_dom)
    save_file(output, new_doc)

if __name__ == '__main__':
    arguments = parse_args()
    target = arguments.target
    xsl = arguments.xsl
    output_file = arguments.output or 'output_transform.html'
    process(target, xsl, output_file)