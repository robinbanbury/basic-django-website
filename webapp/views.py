from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('''<div>
  <h1>Robin's Interests</h1>
</div>
<div>
  <h2>Top 5</h2>
  <p>I was thinking about some <b>'Top 5'</b>s - here's a list I came up with...</p>
  <h3>Films</h3>
  <!-- Unordered list - bullet points -->
  <ul>
    <li>Amelie</li>
    <li>Crash</li>
    <li>Spirited Away</li>
    <li>Big Fish</li>
    <li>The Man Who Sued God</li>
  </ul>

  <!-- Ordered list - numbers / letters -->
  <h3>Albums</h3>
  <ol>
    <li>Dead Silence</li>
    <li>Californication</li>
    <li>Only Revolutions</li>
    <li>Billy Talent II</li>
    <li>De-Loused in the Comatorium</li>
    <li>Notable mentions:
      <ul>
        <li>Puzzle</li>
        <li>BSSM</li>
        <li>Abbey Road</li>
        <li>Good Apollo, I'm Burning Star IV</li>
        <li>Everybody Down</li>
        <li>Revolutions in the Head</li>
      </ul>
    </li>
  </ol>
  <h3>Games</h3>
  <table>
    <tr>
      <th>Title</th>
      <th>Publisher</th>
      <th>Year</th>
    </tr>
    <tr>
      <td>Silent Hill</td>
      <td>Konami</td>
      <td>1999</td>
    </tr>
        <tr>
      <td>Final Fantasy VII</td>
      <td>Square</td>
      <td>1997</td>
    </tr>
        <tr>
      <td>Tekken 3</td>
      <td>Namco</td>
      <td>1998</td>
    </tr>
        <tr>
      <td>MarioKart Wii</td>
      <td>Nintendo</td>
      <td>2008</td>
    </tr>
        <tr>
      <td>Final Fantasy X</td>
      <td>Square</td>
      <td>2002</td>
    </tr>
  </table>
</div>

<div>
  <p>Inspired by <a href="http://dukelearntoprogram.com" taget="blank_">Duke Learn to Program</a></p>
  <p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Cementerio%2C_Tulcán%2C_Ecuador%2C_2015-07-21%2C_DD_60.JPG/500px-Cementerio%2C_Tulcán%2C_Ecuador%2C_2015-07-21%2C_DD_60.JPG" width="20%"/>
</div>''')
