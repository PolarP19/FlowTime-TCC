package com.example.notificacaoexemplo;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;

public class MainActivity extends AppCompatActivity {

    private static final String CHANNEL_ID = "default_channel";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Registra o BroadcastReceiver
        registerReceiver(new NotificationReceiver(), new android.content.IntentFilter("com.example.MY_ACTION"));

        // Envia uma Intent para disparar o BroadcastReceiver
        Intent intent = new Intent();
        intent.setAction("com.example.MY_ACTION");
        intent.putExtra("message", "Você recebeu uma nova notificação!");
        sendBroadcast(intent);
    }

    // BroadcastReceiver interno que vai lidar com a notificação
    public class NotificationReceiver extends BroadcastReceiver {
        @Override
        public void onReceive(Context context, Intent intent) {
            // Recupera a mensagem da Intent
            String message = intent.getStringExtra("message");

            // Cria o canal de notificação para Android 8.0 (API 26) ou superior
            NotificationManager notificationManager = (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                NotificationChannel channel = new NotificationChannel(CHANNEL_ID, "Default Channel", NotificationManager.IMPORTANCE_DEFAULT);
                notificationManager.createNotificationChannel(channel);
            }

            // Cria a notificação
            Notification notification = new NotificationCompat.Builder(context, CHANNEL_ID)
                    .setContentTitle("Nova Mensagem")
                    .setContentText(message)
                    .setSmallIcon(android.R.drawable.ic_dialog_info)
                    .build();

            // Exibe a notificação
            notificationManager.notify(1, notification);

            // Exibe um Toast como exemplo de que a notificação foi disparada
            Toast.makeText(context, "Notificação recebida!", Toast.LENGTH_SHORT).show();
        }
    }
}
