import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});
  @override
  Widget build(BuildContext context) {
    final cards = ['Lista de Compras', 'Nova Compra', 'Upload de Nota', 'Histórico', 'Perfil'];
    return Scaffold(
      appBar: AppBar(title: const Text('SmartMarket')),
      body: GridView.count(
        crossAxisCount: MediaQuery.of(context).size.width > 700 ? 3 : 2,
        children: cards.map((e) => Card(child: Center(child: Text(e)))).toList(),
      ),
    );
  }
}
