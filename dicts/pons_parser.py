import unittest
from enum import Enum
from html.parser import HTMLParser


class TestPonsParser(unittest.TestCase):
    def test_find_translation(self):
        tag_string = """
<dl>
<dt>
pregnancy test
</dt>
<dd>
Schwangerschaftstest
</dd>
</dl>
        """
        tags = {"pregnancy test": ["Schwangerschaftstest"]}
        pons_parser = PonsParser()
        pons_parser.feed(tag_string)
        self.assertEqual(tags, pons_parser.lookup_table)

    def test_find_multiple_translations(self):
        tag_string = """
<dl>
  <dt>
test
  </dt>
<dd>
Untersuchung
</dd>
</dl>
<dl>
  <dt>
      test
  </dt>
  <dd>
Test
  </dd>
</dl>
        """
        tags = {"test": ["Untersuchung", "Test"]}
        pons_parser = PonsParser()
        pons_parser.feed(tag_string)
        self.assertEqual(tags, pons_parser.lookup_table)

    def test_find_actual_translation(self):
        tag_string = """
<dl id="Tdeen1328772" class="dl-horizontal kne first" data-translation="13">
  <dt>
    <div class="dt-inner">
      <ul class="inline translation-options">
<li class="dropdown"><a href="#" class="dropdown-toggle tts trackable trk-audio" data-toggle="dropdown"><i class="icon-volume-down"></i></a><ul class="dropdown-menu"><li><a href="#" class="audio tts trackable trk-audio" data-pons-lang="en_gb"><span class="flag flag_en"></span> Britisches Englisch</a></li><li><a href="#" class="audio tts trackable trk-audio" data-pons-lang="en_us"><span class="flag flag_us"></span> Amerikanisches Englisch</a></li></ul></li>      </ul>
      <div class="source">
<strong class="headword"><a href="/übersetzung?l=deen&amp;q=test&amp;in=en">test</a></strong>      </div>
    </div>
  </dt>
  <dd>
    <div class="dd-inner">
      <div class="target">
<a href="/%C3%BCbersetzung/deutsch-englisch/Untersuchung">Untersuchung</a> <span class="genus"><acronym title="Femininum">f</acronym></span>      </div>
      <ul class="inline translation-options">
<li><a href="#" class="audio tts trackable trk-audio" data-pons-lang="de"><i class="icon-volume-down"></i></a></li><li class="dropdown"><a href="#" data-toggle="dropdown"><i class="icon-plus-sign"></i></a><ul class="dropdown-menu"><li><a href="#" class="favorites"><i class="icon-star"></i>&nbsp;Zu meinen Favoriten hinzufügen</a></li><li><a href="#" class="trainer"><i class="icon-inbox"></i>&nbsp;Für den Vokabeltrainer vormerken</a></li><li><a href="/trainer-import" class="trainer-import"><i class="icon-inbox"></i>&nbsp;Vorgemerkte Vokabeln ansehen</a></li></ul></li>      </ul>
    </div>
  </dd>
  
</dl>
        """
        tags = {"test": ["Untersuchung"]}
        pons_parser = PonsParser()
        pons_parser.feed(tag_string)
        self.assertEqual(tags, pons_parser.lookup_table)


class PonsParserStates(Enum):
    SEARCHING = 0
    IN_DT = 10
    IN_SOURCE = 15
    IN_DD = 20
    IN_TARGET = 25


class PonsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.state = PonsParserStates.SEARCHING
        self.current_key = ""
        self.lookup_table = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'dt':
            self.state = PonsParserStates.IN_DT
        elif tag == 'dd':
            self.state = PonsParserStates.IN_DD
        elif tag == 'div' and \
                self.state == PonsParserStates.IN_DT and \
                ('class', 'source') in attrs:
            self.state = PonsParserStates.IN_SOURCE

    def handle_endtag(self, tag):
        if (tag == 'dt' and self.state == PonsParserStates.IN_DT) or \
                (tag == 'dd' and self.state == PonsParserStates.IN_DD) or \
                (tag == 'div' and self.state == PonsParserStates.IN_SOURCE) or \
                (tag == 'div' and self.state == PonsParserStates.IN_TARGET):
            self.state = PonsParserStates.SEARCHING

    def handle_data(self, data):
        if self.state == PonsParserStates.IN_DT:
            self.current_key = data.strip()
        elif self.state == PonsParserStates.IN_DD:
            self.append_to_lookup_table(data)

    def append_to_lookup_table(self, data):
        if self.current_key not in self.lookup_table:
            self.lookup_table[self.current_key] = []
        self.lookup_table[self.current_key].append(data.strip())


if __name__ == '__main__':
    unittest.main()
