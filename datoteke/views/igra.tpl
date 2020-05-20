% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
  Vislice so najboljša igra za preganjanje dolgčasa.
  </blockquote>

<table>
<tr>
    <td>
        <h2> {{igra.pravilni_del_gesla()}}</h2><br>
    </td>
</tr>
<tr>
    <td>
        <h2> Napačni ugibi: {{igra.nepravilni_ugibi()}} </h2><br>
    </td>
</tr>
<tr>
    <td>
      <img src="../../img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">
      Stopnja obešenosti : {{igra.stevilo_napak()}} / {{model.STEVILO_DOVOLJENIH_NAPAK + 1}} <br>
    </td>
</tr>
</table>


% if poskus == "W":
  <h1> ZMAGAL SI </h1>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif poskus == "X":
  <h1> Izgubil si </h1>

  <h3> Pravilno geslo: {{igra.geslo}} </h3>

  <form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>   

% else:
  <form action="/igra/{{id_igre}}/" method="post">
    Črka: <input type="text" name="crka">
    <button type="submit">Ugibaj novo črko</button>
  </form>

% end

</body>

</html>