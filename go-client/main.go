package main

# pacotes ----------------------------- #
import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)
# ------------------------------------- #

# requisição do log ------------------- #
type LogRequest struct {
	LogLine string `json:"log_line"`
}
# ------------------------------------- #


# resposta API------------------------- #
type AnomalyResponse struct {
	IsAnomaly bool    `json:"is_anomaly"`
	Score     float64 `json:"score"`
}
# ------------------------------------- #

# função principal --------------------------------- #

func main() {
// verifica se o user passou o argumento (a linha do code)
	if len(os.Args) < 2 {
		fmt.Println("Uso: logguardian \"mensagem de log\"")
		return
	}
// captura a mensagem de log passada como args
	logLine := os.Args[1]
	apiURL := os.Getenv("AI_API_URL")
	if apiURL == "" {
		apiURL = "http://ai-service:8000/predict"
	}

// cria o objeto de requisição
	data := LogRequest{LogLine: logLine}

// converte o objeto Go para JSON
	body, _ := json.Marshal(data)

// envia a requisição POST para a API de IA
	resp, err := http.Post(apiURL, "application/json", bytes.NewBuffer(body))
	if err != nil {
		fmt.Println("Erro ao conectar à API:", err)
		return
	}
	defer resp.Body.Close() // garante que o corpo da resposta será fechado

// cria variável para armazenar a resposta
	var result AnomalyResponse

// decodifica o corpo da resposta JSON para a estrutura GO
	json.NewDecoder(resp.Body).Decode(&result)

// define o status de normalidade
	status := "✅ Normal"
	if result.IsAnomaly {
		status = "🚨 Anomalia detectada!"
	}

	fmt.Printf("\n📜 Log: %s\n🔍 Status: %s\n📊 Score: %.4f\n", logLine, status, result.Score)
}
