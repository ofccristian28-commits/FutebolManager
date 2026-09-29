package com.futebolmanager;

import android.app.Activity;
import android.os.Bundle;
import android.graphics.Color;
import android.view.Gravity;
import android.view.View;
import android.widget.*;

public class MainActivity extends Activity {

    LinearLayout tela;
    TextView titulo;
    TextView info;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        menuPrincipal();
    }

    TextView texto(String s, int tamanho) {
        TextView t = new TextView(this);
        t.setText(s);
        t.setTextSize(tamanho);
        t.setTextColor(Color.WHITE);
        t.setGravity(Gravity.CENTER);
        t.setPadding(16, 16, 16, 16);
        return t;
    }

    Button botao(String s) {
        Button b = new Button(this);
        b.setText(s);
        b.setTextSize(16);
        return b;
    }

    void base(String tituloTexto) {
        tela = new LinearLayout(this);
        tela.setOrientation(LinearLayout.VERTICAL);
        tela.setPadding(20, 20, 20, 20);
        tela.setBackgroundColor(Color.rgb(18, 18, 18));

        titulo = texto(tituloTexto, 25);
        titulo.setBackgroundColor(Color.rgb(13, 71, 161));
        tela.addView(titulo,
                new LinearLayout.LayoutParams(-1, 80));

        ScrollView scroll = new ScrollView(this);
        LinearLayout conteudo = new LinearLayout(this);
        conteudo.setOrientation(LinearLayout.VERTICAL);
        conteudo.setPadding(5, 20, 5, 20);
        scroll.addView(conteudo);

        tela.addView(scroll,
                new LinearLayout.LayoutParams(-1, 0, 1));

        info = texto("", 18);
        info.setGravity(Gravity.CENTER);
        conteudo.addView(info);

        setContentView(tela);

        this.conteudo = conteudo;
    }

    LinearLayout conteudo;

    void adicionarBotao(String nome, View.OnClickListener acao) {
        Button b = botao(nome);
        b.setOnClickListener(acao);
        conteudo.addView(b,
                new LinearLayout.LayoutParams(-1, 65));
    }

    void menuPrincipal() {
        base("⚽ FutebolManager");

        info.setText(
            "V1 - Gerenciador de Futebol\\n\\n" +
            "Escolha seu clube para começar."
        );

        adicionarBotao("Santa Cruz", v -> clube("Santa Cruz"));
        adicionarBotao("Sport", v -> clube("Sport"));
        adicionarBotao("Escolher depois", v -> clube("Meu Clube"));
    }

    void clube(String nome) {
        base("⚽ " + nome);

        info.setText(
            "CLUBE: " + nome + "\\n\\n" +
            "Temporada 2026\\n" +
            "Brasileirão\\n" +
            "Copa do Brasil\\n" +
            "Estadual\\n" +
            "Copa do Nordeste"
        );

        adicionarBotao("▶ Próxima rodada", v -> partida(nome));
        adicionarBotao("📋 Elenco", v -> elenco(nome));
        adicionarBotao("🏆 Competições", v -> competicoes(nome));
        adicionarBotao("⬅ Voltar", v -> menuPrincipal());
    }

    void partida(String clube) {
        base("🏟️ Rodada 1");

        info.setText(
            clube + "  x  Adversário\\n\\n" +
            "PLACAR\\n\\n" +
            "0  x  0\\n\\n" +
            "Primeiro tempo"
        );

        adicionarBotao("▶ Continuar partida", v -> intervalo(clube));
        adicionarBotao("⚙ Formação / Tática", v -> {
            Toast.makeText(this, "Formação: 4-3-3", Toast.LENGTH_SHORT).show();
        });
    }

    void intervalo(String clube) {
        base("⏸️ Intervalo");

        info.setText(
            clube + "  0 x 0  Adversário\\n\\n" +
            "Intervalo da partida\\n\\n" +
            "Faça alterações antes do segundo tempo."
        );

        adicionarBotao("🔄 Substituições", v -> {
            Toast.makeText(this, "Substituição realizada", Toast.LENGTH_SHORT).show();
        });

        adicionarBotao("⚙ Mudar formação", v -> {
            Toast.makeText(this, "Formação alterada", Toast.LENGTH_SHORT).show();
        });

        adicionarBotao("▶ Segundo tempo", v -> {
            base("🏟️ Segundo tempo");
            info.setText(
                clube + "  1 x 0  Adversário\\n\\n" +
                "90 minutos\\n\\n" +
                "Vitória!"
            );
            adicionarBotao("▶ Próxima rodada", x -> partida(clube));
            adicionarBotao("⬅ Menu do clube", x -> clube(clube));
        });
    }

    void elenco(String clube) {
        base("👥 Elenco - " + clube);

        info.setText(
            "GOLEIRO\\n" +
            "Goleiro 1\\n\\n" +
            "DEFESA\\n" +
            "Zagueiro 1\\n" +
            "Zagueiro 2\\n" +
            "Lateral 1\\n" +
            "Lateral 2\\n\\n" +
            "MEIO-CAMPO\\n" +
            "Volante 1\\n" +
            "Meia 1\\n" +
            "Meia 2\\n\\n" +
            "ATAQUE\\n" +
            "Ponta 1\\n" +
            "Atacante 1\\n" +
            "Atacante 2"
        );

        adicionarBotao("⬅ Voltar", v -> clube(clube));
    }

    void competicoes(String clube) {
        base("🏆 Competições");

        info.setText(
            "Brasileirão Série A\\n\\n" +
            "Copa do Brasil\\n\\n" +
            "Campeonato Estadual\\n\\n" +
            "Copa do Nordeste\\n\\n" +
            "Promoção e rebaixamento"
        );

        adicionarBotao("⬅ Voltar", v -> clube(clube));
    }
}
