void setup() {
  size(1200, 300);
}


String[] Document = loadStrings("/home/arosa/Desktop/app/perfil.txt");
String[] DocumentPrevisao = loadStrings("/home/arosa/Desktop/app/previsao.txt");
boolean readingLine = true;
boolean readingLinePrevisao = true;
int j, jPrevisao, count = 0;
ArrayList<Integer> temperatures = new ArrayList<Integer>();
ArrayList<Float> values = new ArrayList<Float>();
ArrayList<Float> previsao = new ArrayList<Float>();
boolean firstRun = true;

void draw() {
  background(255);

  if (firstRun) {
    // ARQUIVO UM
    for (int i = 0; i < Document.length ; i++) {//varrendo as linhas
      j = 0;
      readingLine  = true;
      while (readingLine) {
        if (Document[i].charAt(j) == ':') {
          //println(j);
          //println(count);
          //println(Integer.parseInt(Document[i].substring(0,j)));
          temperatures.add(Integer.parseInt(Document[i].substring(0, j)));
          values.add(Float.parseFloat(Document[i].substring(j+1, Document[i].length())));
        }
        //println(Document[i].charAt(j));
        //println("-");
        if (Document[i].length() == j+1) {
          //println("entrei aqui");
          readingLine = false;
          break;
        }
        j++;
      }
    }

    //ARQUIVO DOIS
    for (int i = 0; i < DocumentPrevisao.length ; i++) {//varrendo as linhas
      jPrevisao = 0;
      readingLinePrevisao  = true;
      while (readingLinePrevisao) {
        if (DocumentPrevisao[i].charAt(jPrevisao) == ':') {
          //println(j);
          //println(count);
          //println(Integer.parseInt(Document[i].substring(0,j)));
          previsao.add(Float.parseFloat(DocumentPrevisao[i].substring(jPrevisao+1, DocumentPrevisao[i].length())));
        }
        //println(Document[i].charAt(j));
        //println("-");
        if (DocumentPrevisao[i].length() == jPrevisao+1) {
          //println("entrei aqui");
          readingLinePrevisao = false;
          break;
        }
        jPrevisao++;
      }
    }

    firstRun = false;
  }
  for (int i = 0 ; i < temperatures.size() ; i++) {
    println("Temperatura - "+temperatures.get(i)+" - Valor - "+values.get(i));
  } //somente para debug

  //GRAFICO DA DIREITA

  float barHeight, barWidth, barGap, x, y;
  float maxValue = Float.MIN_VALUE;
  float maxPrevisao = Float.MIN_VALUE;
  boolean selected = false;

  if (temperatures.isEmpty()) {
    text("Please, wait for the statistics...", 550, 150);
  }
  else {
    strokeWeight(1);
    line(750.0, 200.0, 750.0, 50.0);
    line(750.0, 200.0, 1150.0, 200.0);

    barGap = 5;
    x = 750;
    for (int i = 0; i < previsao.size(); i++) {
      if (previsao.get(i) > maxPrevisao)
        maxPrevisao = previsao.get(i);
    }

    barWidth = (700 - previsao.size()*barGap)/previsao.size()*0.5;
    for (int i = 0; i < temperatures.size(); i++) {
      if (mouseY <=300) {
        if (mouseX>x && mouseX<=x+barGap+barWidth) {
          fill(0);
          text(temperatures.get(i), mouseX, mouseY);
          fill(216, 223, 234);
          selected = true;
          barHeight = map(previsao.get(i), 0, maxPrevisao*1.5, 0, 200);
          fill(0);
          text(previsao.get(i)+"-", 650, 200-barHeight);
          fill(216, 223, 234);
        }
        else {
          selected = false;
        }
      }
      if (!selected)
        fill(109, 132, 180);
      barHeight = map(previsao.get(i), 0, maxPrevisao*1.5, 0, 200);
      //text(values.get(i)+"-", 380, 200-barHeight);
      //fill(109, 132, 180);
      rect(x+barGap, 200-barHeight, barWidth, barHeight);
      x+=barGap+barWidth;
    }
  }

  text("Grafico Temperatura x Vendas", 250, 250);
  // GRAFICO DA ESQUERDA
  if (temperatures.isEmpty()) {
    text("Please, wait for the statistics...", 550, 150);
  }
  else {
    strokeWeight(1);
    line(150.0, 200.0, 150.0, 50.0);
    line(150.0, 200.0, 550.0, 200.0);

    barGap = 5;
    x = 150;
    for (int i = 0; i < values.size(); i++) {
      if (temperatures.get(i) > maxValue)
        maxValue = values.get(i);
    }

    barWidth = (700 - values.size()*barGap)/values.size()*0.5;
    for (int i = 0; i < temperatures.size(); i++) {
      if (mouseY <=300) {
        if (mouseX>x && mouseX<=x+barGap+barWidth) {
          fill(0);
          text(temperatures.get(i), mouseX, mouseY);
          fill(216, 223, 234);
          selected = true;
          barHeight = map(values.get(i), 0, maxValue*1.5, 0, 200);
          fill(0);
          text(values.get(i)+"-", 50, 200-barHeight);
          fill(216, 223, 234);
        }
        else {
          selected = false;
        }
      }
      if (!selected)
        fill(109, 132, 180);
      barHeight = map(values.get(i), 0, maxValue*1.5, 0, 200);
      //text(values.get(i)+"-", 380, 200-barHeight);
      //fill(109, 132, 180);
      rect(x+barGap, 200-barHeight, barWidth, barHeight);
      x+=barGap+barWidth;
    }
  }
  text("Grafico Temperatura x Previsao Vendas", 850, 250);
  rotate(-HALF_PI);
  text("Make things Alive",0,0);
}

