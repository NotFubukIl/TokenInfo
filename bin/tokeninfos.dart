import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';

String FileContent = ""!;
class Allah {
  static Future<String> main() async {
    print("Token ?: ");
    final token = stdin.readLineSync()!;
    final al = await Allah.getMainInfos(token);
    if (al == false) {
      print("Token Isn't Valid");
      exit(0);
    }
    final settings = await Allah.getSettingsInfos(token);
    final connections = await Allah.getConnections(token);
    final kdo = await Allah.getKdo(token);

    for (final p in al.keys) {
      var f = al[p];
      if (f == null) f = "";
      FileContent += ("[$p]: $f") + "\n";
    }
    for (final p in settings.keys) {
      var f = settings[p];
      if (f == null) f = "";
       FileContent += ("[$p]: $f") + "\n";
    }
    for (final p in connections) {
      for (final n in p.keys) {
        final z = p[n];
         FileContent += ("[$n]: $z") + "\n";
      }
    }
    for (final p in kdo) {
      for (final n in p.keys) {
        final z = p[n];
         FileContent += ("[$n]: $z") + "\n";
      }
    }

    File("./infos-" + token.split(".")[0] + ".txt").writeAsStringSync(FileContent);
    return "./infos-" + token.split(".")[0] + ".txt";
  }

  static Future<dynamic> getMainInfos(String token) async {
    final response = await http.get(
      Uri.parse("https://discord.com/api/v9/users/@me"),
      headers: {"authorization": token},
    );
    final j = jsonDecode(response.body);
    if (j.containsKey("message")) {
      return false;
    } else {
      return j;
    }
  }

  static Future<dynamic> getSettingsInfos(String token) async {
    final response = await http.get(
      Uri.parse("https://discord.com/api/v9/users/@me/settings"),
      headers: {"authorization": token},
    );
    final j = jsonDecode(response.body);
    if (j.containsKey("message")) {
      return false;
    } else {
      return j;
    }
  }

  static Future<dynamic> getConnections(String token) async {
    final response = await http.get(
      Uri.parse("https://discordapp.com/api/v9/users/@me/connections"),
      headers: {"authorization": token},
    );
    final j = jsonDecode(response.body);
    if (response.body.contains("message")) {
      return false;
    } else {
      return j;
    }
  }

  static Future<dynamic> getKdo(String token) async {
    final response = await http.get(
      Uri.parse("https://discord.com/api/v8/users/@me/entitlements/gifts"),
      headers: {"authorization": token},
    );
    final j = jsonDecode(response.body);
    if (response.body.contains("message")) {
      return false;
    } else {
      return j;
    }
  }
}

void main() async {
  final filePath = await Allah.main();
  print("Infos in $filePath");
  stdin.readLineSync();
}