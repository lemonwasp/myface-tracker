window.onload = async function() {
  const user_id = localStorage.getItem('user_id');
  if (!user_id) {
      alert('로그인이 필요합니다.');
      window.location.href = 'login.html';
      return;
  }

  const response = await fetch(`http://127.0.0.1:8000/records/${user_id}`);
  if (response.ok) {
      const records = await response.json();
      const list = document.getElementById('recordList');
      list.innerHTML = '';  // 기존 리스트 초기화

      const labels = [];
      const flowScores = [];

      records.forEach(record => {
          const item = document.createElement('li');
          item.textContent = `${record.timestamp} - ${record.activity_name} (${record.emotion}) 몰입도: ${record.flow_score}`;
          list.appendChild(item);

          // 차트 데이터 준비
          labels.push(record.timestamp);
          flowScores.push(record.flow_score);
      });

      // 차트 그리기
      const ctx = document.getElementById('flowChart').getContext('2d');
      const flowChart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: labels,
              datasets: [{
                  label: '몰입도 변화',
                  data: flowScores,
                  borderColor: 'blue',
                  fill: false
              }]
          }
      });

  } else {
      alert('기록을 불러오지 못했습니다.');
  }
};